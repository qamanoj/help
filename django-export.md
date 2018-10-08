---------------------------------------------django export import csv--------------------------------------------------------

pip install django-import-export
  
    INSTALLED_APPS = (
      ...
      'import_export',
    )

    from import_export import resources
    from import_export.admin import ImportExportModelAdmin, ExportMixin


    class RegistrationOTPResource(resources.ModelResource):
        class Meta:
            model = RegistrationOTP
            fields = ('id','phone_number','otp','created_date','is_verified','country__name')
            export_order = ('id','country__name','phone_number','otp','created_date','is_verified')

        def get_queryset(self, request):
          return super(RegistrationOTPResource, self).get_queryset(request).select_related('country')


    class RegistrationOTPAdmin(ImportExportModelAdmin, admin.ModelAdmin):
      list_display = ('id', 'phone_number', 'otp', 'created_date', 'is_verified', )
      list_filter = ('is_verified', ('created_date', DateRangeFilter))
      search_fields = ('id', 'phone_number', 'otp')
      resource_class = RegistrationOTPResource

    admin.site.register(RegistrationOTP, RegistrationOTPAdmin)
