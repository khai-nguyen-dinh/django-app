from django.conf.urls import url
from .views import (KhoaListAPIView,
                    KhoaCreateAPIView,
                    KhoaUpdateAPIView,
                    KhoaDetailAPIView,
                    KhoaDeleteAPIView)
from .views import (LopListAPIView,
                    LopDetailAPIView,
                    LopCreateAPIView,
                    LopUpdateAPIView,
                    LopDeleteAPIView)
from .views import (MonHocListAPIView,
                    MonHocDetailAPIView,
                    MonHocCreateAPIView,
                    MonHocUpdateAPIView,
                    MonHocDeleteAPIView)
from .views import (SinhVienListAPIView,
                    SinhVienDetailAPIView,
                    SinhVienCreateAPIView,
                    SinhVienUpdateAPIView,
                    SinhVienDeleteAPIView)
from .views import (KetQuaListAPIView,
                    KetQuaDetailAPIView,
                    KetQuaCreateAPIView,
                    KetQuaUpdateAPIView,
                    KetQuaDeleteAPIView)

urlpatterns = [
    # khoa
    url(r'^khoa/$', KhoaListAPIView.as_view(), name='list_khoa'),
    url(r'^khoa/create/$', KhoaCreateAPIView.as_view(), name='create_khoa'),
    url(r'^khoa/update/(?P<pk>[\w-]+)/$', KhoaUpdateAPIView.as_view(), name='update_khoa'),
    url(r'^khoa/detail/(?P<pk>[\w-]+)/$', KhoaDetailAPIView.as_view(), name='detail_khoa'),
    url(r'^khoa/delete/(?P<pk>[\w-]+)/$', KhoaDeleteAPIView.as_view(), name='delete_khoa'),

    # lop
    url(r'^lop/$', LopListAPIView.as_view(), name='list_lop'),
    url(r'^lop/detail/(?P<pk>[\w-]+)/$', LopDetailAPIView.as_view(), name='detail_lop'),
    url(r'^lop/create/$', LopCreateAPIView.as_view(), name='create_lop'),
    url(r'^lop/update/(?P<pk>[\w-]+)/$', LopUpdateAPIView.as_view(), name='update_lop'),
    url(r'^lop/delete/(?P<pk>[\w-]+)/$', LopDeleteAPIView.as_view(), name='delete_lop'),

    # sinhvien
    url(r'^sinhvien/', SinhVienListAPIView.as_view(), name='list_sinhvien'),
    url(r'^sinhvien/detail/(?P<abc>[\w-]+)/$', SinhVienDetailAPIView.as_view(), name='detail_sinhvien'),
    url(r'^sinhvien/create/$', SinhVienCreateAPIView.as_view(), name='create_sinhvien'),
    url(r'^sinhvien/update/(?P<pk>[\w-]+)/$', SinhVienUpdateAPIView.as_view(), name='update_sinhvien'),
    url(r'^sinhvien/delete/(?P<pk>[\w-]+)/$', SinhVienDeleteAPIView.as_view(), name='delete_sinhvien'),

    # monhoc
    url(r'^monhoc/$', MonHocListAPIView.as_view(), name='list_monhoc'),
    url(r'^monhoc/detail/(?P<tenmh>[\w-]+)/$', MonHocDetailAPIView.as_view(), name='detail_monhoc'),
    url(r'^monhoc/create/$', MonHocCreateAPIView.as_view(), name='create_monhoc'),
    url(r'^monhoc/update/(?P<pk>[\w-]+)/$', MonHocUpdateAPIView.as_view(), name='update_monhoc'),
    url(r'^monhoc/delete/(?P<pk>[\w-]+)/$', MonHocDeleteAPIView.as_view(), name='delete_monhoc'),

    #ketqua
    url(r'^ketqua/$', KetQuaListAPIView.as_view(), name='list_ketqua'),
    url(r'^ketqua/detail/(?P<pk>[\w-]+)/$', KetQuaDetailAPIView.as_view(), name='detail_ketqua'),
    url(r'^ketqua/create/$', KetQuaCreateAPIView.as_view(), name='create_ketqua'),
    url(r'^ketqua/update/(?P<pk>[\w-]+)/$', KetQuaUpdateAPIView.as_view(), name='update_ketqua'),
    url(r'^ketqua/delete/(?P<pk>[\w-]+)/$', KetQuaDeleteAPIView.as_view(), name='delete_ketqua'),
]
