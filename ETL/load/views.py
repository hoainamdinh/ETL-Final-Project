from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Customer, Product, Order

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        try:
            # Read the file directly from memory
            df = load_data(uploaded_file)

            # Process different types of data
            if 'customer_id' in df.columns:
                load_customers(df)
            if 'product_id' in df.columns:
                load_products(df)
            if 'order_id' in df.columns:
                load_orders(df)

        except Exception as e:
            print(f"❌ Error processing file: {e}")

    return render(request, 'upload.html')


def display_data(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'display.html', {'customers': customers, 'products': products, 'orders': orders})


# 🔹 Function: Read data from file (CSV, Excel, JSON)
def load_data(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith('.xls') or file_name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif file_name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif file_name.endswith('.json'):
        df = pd.read_json(uploaded_file)
    else:
        raise ValueError("📂 Unsupported file format!")

    print("📊 Uploaded Data:", df.head())  # Debugging
    return df


# 🔹 Function: Load customer data into DB
def load_customers(df):
    if not all(col in df.columns for col in ['customer_id', 'name', 'email', 'location']):
        print("⚠️ Missing customer data columns!")
        return

    for _, row in df.iterrows():
        Customer.objects.update_or_create(
            customer_id=row['customer_id'],
            defaults={
                'name': row['name'],
                'email': row['email'],
                'location': row['location']
            }
        )


# 🔹 Function: Load product data into DB
def load_products(df):
    if not all(col in df.columns for col in ['product_id', 'name', 'category', 'price']):
        print("⚠️ Missing product data columns!")
        return

    for _, row in df.iterrows():
        Product.objects.update_or_create(
            product_id=row['product_id'],
            defaults={
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            }
        )


# 🔹 Function: Load order data into DB
def load_orders(df):
    if not all(col in df.columns for col in ['order_id', 'customer_id', 'product_id', 'order_date', 'quantity', 'total_amount']):
        print("⚠️ Missing order data columns!")
        return

    for _, row in df.iterrows():
        customer, _ = Customer.objects.get_or_create(customer_id=row['customer_id'])
        product, _ = Product.objects.get_or_create(product_id=row['product_id'])

        Order.objects.update_or_create(
            order_id=row['order_id'],
            defaults={
                'customer': customer,
                'product': product,
                'order_date': row['order_date'],
                'quantity': row['quantity'],
                'total_amount': row['total_amount']
            }
        )


def display_data(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'display.html', {'customers': customers, 'products': products, 'orders': orders})