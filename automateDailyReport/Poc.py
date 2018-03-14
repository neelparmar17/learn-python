loc_id = Hub.objects.filter(supplier_type__iexact="HUB", status="Active").values('name', 'supplier_ptr_id')
    # print(hub[0])
    for lid in loc_id:
        vids = SupplierLocation.objects.filter(supplier_id=lid['supplier_ptr_id']).values('village_id')
        for vid in vids:
            com_name = Location.objects.filter(id=vid['village_id']).values('complete_name')
            print(lid['name'] +" ==== " +com_name[0]["complete_name"])



sup_id = SupplierLocation.objects.select_related('supplier_id').filter(supplier__supplier_type__iexact="HUB", supplier__hub__status="Active").select_related('village_id').values('village_id','supplier_id', 'supplier__hub__name', 'village__complete_name')