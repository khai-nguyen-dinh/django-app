from django.db import models


class Khoa(models.Model):
    makhoa = models.CharField(max_length=100,primary_key=True)
    tenkhoa = models.CharField(max_length=100)
    def __str__(self):
        return self.tenkhoa

class Lop(models.Model):
    malop = models.CharField(max_length=100,primary_key=True)
    tenlop = models.CharField(max_length=100)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE,related_name='lop')

    def __str__(self):
        return self.tenlop


class SinhVien(models.Model):
    masv = models.CharField(max_length=100, primary_key=True)
    hoten = models.CharField(max_length=100)
    gioitinh = models.CharField(max_length=3, default='Nam')
    ngaysinh = models.DateField(null=True, blank=True)
    hocbong = models.BooleanField(default=False)
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE,related_name='sinhvien')
    def __str__(self):
        return self.hoten

class MonHoc(models.Model):
    mamh = models.CharField(max_length=100,primary_key=True)
    tenmh = models.CharField(max_length=100)
    sotiet = models.IntegerField(default=0)
    sinhvien = models.ManyToManyField(SinhVien, through='KetQua')

    def __str__(self):
        return self.tenmh

class KetQua(models.Model):
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE,related_name='sinhvien')
    monhoc = models.ForeignKey(MonHoc, on_delete=models.CASCADE,related_name='monhoc')
    diemthi = models.FloatField(default=0.0)