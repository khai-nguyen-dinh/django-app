from rest_framework.serializers import ModelSerializer

from rest.models import (Khoa,
                         Lop,
                         SinhVien,
                         MonHoc,
                         KetQua)


class SinhVienSerializer(ModelSerializer):

    class Meta:
        model = SinhVien
        fields = ('masv',
                  'hoten',
                  'gioitinh',
                  'ngaysinh',
                  'hocbong',
                  )



class LopSerializer(ModelSerializer):
    sinhvien = SinhVienSerializer(many=True)

    class Meta:
        model = Lop
        fields = ('malop',
                  'tenlop',
                  'khoa',
                  'sinhvien',
                  )


class KhoaSerializer(ModelSerializer):
    # lop = SerializerMethodField()
    lop = LopSerializer(many=True, read_only=True)

    class Meta:
        model = Khoa
        fields = ('makhoa',
                  'tenkhoa',
                  'lop',
                  )

        # def get_lop(self, obj):
        #     return LopSerializer(Lop.objects.filter(khoa=obj), many=True).data


class MonHocSerializer(ModelSerializer):
    class Meta:
        model = MonHoc
        fields = ('mamh',
                  'tenmh',
                  'sotiet',
                  )


class KetQuaSerializer(ModelSerializer):
    sinhvien = SinhVienSerializer
    monhoc = MonHocSerializer
    class Meta:
        model = KetQua
        fields = ('sinhvien',
                  'monhoc',
                  'diemthi',
                  )
