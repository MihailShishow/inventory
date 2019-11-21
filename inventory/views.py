from django.shortcuts import render
from .models import Product, ProductCategory, Counterparty,\
    IncomeWarrant, OutcomeWarrant, IncomeInvoice, OutcomeInvoice
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .util_functions import str_to_date
from decimal import Decimal
from django.http import Http404
from django.db.models import ProtectedError
from rest_framework.generics import get_object_or_404
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            self.perform_destroy(product)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ProtectedError:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CounterpartyViewSet(viewsets.ModelViewSet):
    queryset = Counterparty.objects.all().order_by('name')
    serializer_class = CounterpartySerializer

    def destroy(self, request, *args, **kwargs):
        try:
            counterparty = self.get_object()
            self.perform_destroy(counterparty)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)


class IncomeWarrantViewSet(viewsets.ModelViewSet):
    queryset = IncomeWarrant.objects.all().order_by('issued_date')
    serializer_class = IncomeWarrantSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            warrant = self.get_object()
            if not warrant.registered:
                self.perform_destroy(warrant)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            saved_warrant = self.get_object()
            if not saved_warrant.registered:
                data = request.data
                serializer = IncomeWarrantSerializer(
                    saved_warrant, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                if 'registered' in data:
                    serializer = IncomeWarrantSerializer(
                        saved_warrant, data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status.HTTP_404_NOT_FOUND)


class OutcomeWarrantViewSet(viewsets.ModelViewSet):
    queryset = OutcomeWarrant.objects.all().order_by('issued_date')
    serializer_class = OutcomeWarrantSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            warrant = self.get_object()
            if not warrant.registered:
                self.perform_destroy(warrant)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            saved_warrant = self.get_object()
            if not saved_warrant.registered:
                data = request.data
                serializer = OutcomeWarrantSerializer(
                    saved_warrant, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                if 'registered' in data:
                    serializer = OutcomeWarrantSerializer(
                        saved_warrant, data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status.HTTP_404_NOT_FOUND)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all().order_by('name')
    serializer_class = ProductCategorySerializer


class IncomeInvoiceViewSet(viewsets.ModelViewSet):
    queryset = IncomeInvoice.objects.all().order_by('issued_date')
    serializer_class = IncomeInvoiceSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            invoice = self.get_object()
            if not invoice.registered:
                self.perform_destroy(invoice)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            saved_invoice = self.get_object()
            if not saved_invoice.registered:
                data = request.data
                serializer = IncomeInvoiceSerializer(
                    saved_invoice, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                if 'registered' in data:
                    serializer = IncomeInvoiceSerializer(
                        saved_invoice, data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status.HTTP_404_NOT_FOUND)


class OutcomeInvoiceViewSet(viewsets.ModelViewSet):
    queryset = OutcomeInvoice.objects.all().order_by('issued_date')
    serializer_class = OutcomeInvoiceSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            invoice = self.get_object()
            if not invoice.registered:
                self.perform_destroy(invoice)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            saved_invoice = self.get_object()
            if not saved_invoice.registered:
                data = request.data
                serializer = OutcomeInvoiceSerializer(
                    saved_invoice, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                if 'registered' in data:
                    serializer = OutcomeInvoiceSerializer(
                        saved_invoice, data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status.HTTP_404_NOT_FOUND)


class ProductIncomeViewSet(viewsets.ModelViewSet):
    queryset = ProductIncome.objects.all()
    serializer_class = ProductIncomeSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            pincome = self.get_object()
            if not pincome.invoice.registered:
                self.perform_destroy(pincome)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            saved_income = self.get_object()
            if not saved_income.invoice.registered:
                data = request.data
                serializer = ProductIncomeSerializer(
                    saved_income, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status.HTTP_404_NOT_FOUND)


class ProductOutcomeViewSet(viewsets.ModelViewSet):
    queryset = ProductOutcome.objects.all()
    serializer_class = ProductOutcomeSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            poutcome = self.get_object()
            if not poutcome.invoice.registered:
                self.perform_destroy(poutcome)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            saved_outcome = self.get_object()
            if not saved_outcome.invoice.registered:
                data = request.data
                serializer = ProductOutcomeSerializer(
                    saved_outcome, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Http404:
            return Response(status.HTTP_404_NOT_FOUND)


class ProductCirculationByDateRange(APIView):

    def get(self, request, pk, start, end):
        start_date = str_to_date(start)
        end_date = str_to_date(end)

        if start_date > end_date:
            return Response(data={'error': 'Wrong order of dates.'},
                            status=400)
        else:
            context = {'request': request,
                       'start_date': start_date, 'end_date': end_date}
            product = get_object_or_404(Product.objects.all(), pk=pk)
            serializer = ProductReportSerializer(product, context=context)
            return Response({'data': serializer.data})


class CounterpartySummaryByDateRange(APIView):

    def get(self, request, pk, start, end):
        start_date = str_to_date(start)
        end_date = str_to_date(end)

        if start_date > end_date:
            return Response(data={'error': 'Wrong order of dates.'},
                            status=400)
        else:
            context = {'request': request,
                       'start_date': start_date, 'end_date': end_date}
            counterparty = get_object_or_404(Counterparty.objects.all(), pk=pk)
            serializer = CounterpartyReportSerializer(
                counterparty, context=context)
            return Response({'data': serializer.data})
