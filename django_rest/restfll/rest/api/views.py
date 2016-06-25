from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveAPIView,
                                     RetrieveDestroyAPIView)
from rest.models import (Khoa,
                         Lop,
                         SinhVien,
                         MonHoc,
                         KetQua)
from .serializers import (KhoaSerializer,
                          LopSerializer,
                          SinhVienSerializer,
                          MonHocSerializer,
                          KetQuaSerializer)


# Khoa
class KhoaListAPIView(ListAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer


class KhoaCreateAPIView(CreateAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer


class KhoaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer


class KhoaDetailAPIView(RetrieveAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer
    lookup_url_kwarg = 'abc'

class KhoaDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer


# Lop

class LopListAPIView(ListAPIView):
    queryset = Lop.objects.all()
    serializer_class = LopSerializer


class LopCreateAPIView(CreateAPIView):
    queryset = Lop.objects.all()
    serializer_class = LopSerializer


class LopUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Lop.objects.all()
    serializer_class = LopSerializer


class LopDetailAPIView(RetrieveAPIView):
    queryset = Lop.objects.all()
    serializer_class = LopSerializer


class LopDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Lop.objects.all()
    serializer_class = LopSerializer


# SinhVien
class SinhVienListAPIView(ListAPIView):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer


class SinhVienCreateAPIView(CreateAPIView):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer


class SinhVienUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer


class SinhVienDetailAPIView(RetrieveAPIView):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer


class SinhVienDeleteAPIView(RetrieveDestroyAPIView):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer

#monhoc
class MonHocListAPIView(ListAPIView):
    queryset = MonHoc.objects.all()
    serializer_class = MonHocSerializer


class MonHocCreateAPIView(CreateAPIView):
    queryset = MonHoc.objects.all()
    serializer_class = MonHocSerializer


class MonHocUpdateAPIView(RetrieveUpdateAPIView):
    queryset = MonHoc.objects.all()
    serializer_class = MonHocSerializer


class MonHocDetailAPIView(RetrieveAPIView):
    queryset = MonHoc.objects.all()
    serializer_class = MonHocSerializer
    lookup_field = 'tenmh'

class MonHocDeleteAPIView(RetrieveDestroyAPIView):
    queryset = MonHoc.objects.all()
    serializer_class = MonHocSerializer

#ketqua
class KetQuaListAPIView(ListAPIView):
    queryset = KetQua.objects.all()
    serializer_class = KetQuaSerializer


class KetQuaCreateAPIView(CreateAPIView):
    queryset = KetQua.objects.all()
    serializer_class = KetQuaSerializer


class KetQuaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = KetQua.objects.all()
    serializer_class = KetQuaSerializer


class KetQuaDetailAPIView(RetrieveAPIView):
    queryset = KetQua.objects.all()
    serializer_class = KetQuaSerializer


class KetQuaDeleteAPIView(RetrieveDestroyAPIView):
    queryset = KetQua.objects.all()
    serializer_class = KetQuaSerializer
