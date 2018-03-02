# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AggregatorBankAccounts(models.Model):
    bankaccount_ptr = models.ForeignKey('BankAccounts', models.DO_NOTHING, primary_key=True)
    account_verified = models.IntegerField()
    aggregator = models.ForeignKey('Aggregators', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aggregator_bank_accounts'


class AggregatorDocuments(models.Model):
    document = models.CharField(max_length=100, blank=True, null=True)
    verification_status = models.CharField(max_length=15, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    aggregator = models.ForeignKey('Aggregators', models.DO_NOTHING)
    document_type = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'aggregator_documents'


class AggregatorOnboardings(models.Model):
    terms_accepted = models.IntegerField()
    terms_accepted_on = models.DateTimeField()
    aggregator = models.ForeignKey('Aggregators', models.DO_NOTHING)
    status = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    verified_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    verified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aggregator_onboardings'


class AggregatorOwners(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    aggregator = models.ForeignKey('Aggregators', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aggregator_owners'


class Aggregators(models.Model):
    supplier_ptr = models.ForeignKey('Suppliers', models.DO_NOTHING, primary_key=True)
    category = models.CharField(max_length=15)
    source = models.CharField(max_length=15)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aggregators'


class AppConfigurations(models.Model):
    key = models.CharField(unique=True, max_length=56)
    value = models.CharField(max_length=56)

    class Meta:
        managed = False
        db_table = 'app_configurations'


class Applicants(models.Model):
    phone_number = models.CharField(unique=True, max_length=15)
    village = models.CharField(max_length=30, blank=True, null=True)
    taluka = models.CharField(max_length=30, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicants'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BankAccounts(models.Model):
    account_holder = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=11)
    account_number = models.CharField(max_length=30)
    pan_number = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'bank_accounts'


class CampaignConstraintTypes(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'campaign_constraint_types'


class Commissions(models.Model):
    commission_percentage = models.FloatField()

    class Meta:
        managed = False
        db_table = 'commissions'


class CropSoils(models.Model):
    crop = models.ForeignKey('Crops', models.DO_NOTHING)
    soil = models.ForeignKey('SoilTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crop_soils'


class Crops(models.Model):
    name = models.CharField(max_length=15)
    resource_key = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crops'


class Currencies(models.Model):
    name = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'currencies'


class DailyPerformanceSummary(models.Model):
    order_source = models.CharField(max_length=30, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    total_orders = models.IntegerField(blank=True, null=True)
    total_invoiced = models.FloatField(blank=True, null=True)
    total_acres = models.FloatField(blank=True, null=True)
    hub = models.ForeignKey('Hubs', models.DO_NOTHING, blank=True, null=True)
    implement_id = models.IntegerField(blank=True, null=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    last_synced_at = models.DateTimeField()
    total_minutes = models.IntegerField(blank=True, null=True)
    total_collected = models.FloatField(blank=True, null=True)
    total_minutes_operated = models.IntegerField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    implement_spec = models.ForeignKey('ImplementSpecs', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_performance_summary'


class DistrictLocations(models.Model):
    district_id = models.CharField(max_length=5)
    location = models.ForeignKey('Locations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'district_locations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=64)
    hour = models.CharField(max_length=64)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=64)
    month_of_year = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.PositiveIntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoFsmLogStatelog(models.Model):
    timestamp = models.DateTimeField()
    state = models.CharField(max_length=255)
    transition = models.CharField(max_length=255)
    object_id = models.PositiveIntegerField()
    by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_fsm_log_statelog'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EquipmentPriceLists(models.Model):
    equipment_pricing = models.IntegerField()
    price_list = models.ForeignKey('PriceLists', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'equipment_price_lists'


class EquipmentPricing(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currencies, models.DO_NOTHING)
    sku = models.ForeignKey('Sku', models.DO_NOTHING)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField()
    is_active = models.IntegerField()
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField()
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_pricing'


class EquipmentPricingEnquiry(models.Model):
    phone_of_enquirer = models.CharField(max_length=15)
    implement_type_name = models.CharField(max_length=30)
    enquired_on = models.DateTimeField()
    duration = models.FloatField(blank=True, null=True)
    operational_area = models.FloatField(blank=True, null=True)
    promotion = models.PositiveIntegerField(blank=True, null=True)
    estimated_price = models.CharField(max_length=30, blank=True, null=True)
    name_of_enquirer = models.CharField(max_length=128, blank=True, null=True)
    implement_spec_name = models.CharField(max_length=30, blank=True, null=True)
    operation_area_unit = models.CharField(max_length=15, blank=True, null=True)
    implement_brand_name = models.CharField(max_length=40, blank=True, null=True)
    implement_pricing_model_name = models.CharField(max_length=30, blank=True, null=True)
    duration_unit = models.CharField(max_length=15, blank=True, null=True)
    soil_condition = models.CharField(max_length=10, blank=True, null=True)
    cca_agent_name = models.CharField(max_length=128)
    extras = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_pricing_enquiry'


class FarmLands(models.Model):
    area = models.FloatField()
    landmark = models.CharField(max_length=100, blank=True, null=True)
    plot_number = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.ForeignKey('Locations', models.DO_NOTHING)
    measurement_unit = models.ForeignKey('MeasurementUnits', models.DO_NOTHING)
    owner = models.ForeignKey('Farmers', models.DO_NOTHING)
    operational_area = models.FloatField(blank=True, null=True)
    street_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farm_lands'


class FarmerCommunities(models.Model):
    added_on = models.DateTimeField()
    farmer = models.ForeignKey('Farmers', models.DO_NOTHING)
    friend = models.ForeignKey('Farmers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'farmer_communities'
        unique_together = (('farmer', 'friend'),)


class FarmerLocation(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    farmer = models.ForeignKey('Farmers', models.DO_NOTHING)
    village = models.ForeignKey('Locations', models.DO_NOTHING)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    plot_number = models.CharField(max_length=30, blank=True, null=True)
    street_name = models.CharField(max_length=128, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_location'


class FarmerOrderFeedbackOptions(models.Model):
    option = models.CharField(max_length=255)
    resource_key = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmer_order_feedback_options'


class Farmers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    source = models.CharField(max_length=100, blank=True, null=True)
    referrer = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmers'


class FarmersFarmlandcrop(models.Model):
    crop = models.ForeignKey(Crops, models.DO_NOTHING)
    farmland = models.ForeignKey(FarmLands, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'farmers_farmlandcrop'


class FarmingStages(models.Model):
    name = models.CharField(max_length=30)
    rank = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'farming_stages'


class FranchiseeHubs(models.Model):
    is_active = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    franchisee = models.ForeignKey('Franchisees', models.DO_NOTHING)
    hub = models.ForeignKey('Hubs', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'franchisee_hubs'
        unique_together = (('hub', 'is_active'),)


class FranchiseeOwners(models.Model):
    franchisee = models.ForeignKey('Franchisees', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'franchisee_owners'


class FranchiseeTypes(models.Model):
    type = models.CharField(max_length=15)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'franchisee_types'


class Franchisees(models.Model):
    franchisee_code = models.CharField(unique=True, max_length=15, blank=True, null=True)
    is_active = models.IntegerField()
    franchisee_type = models.ForeignKey(FranchiseeTypes, models.DO_NOTHING)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'franchisees'


class HealthCheckDbTestmodel(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'health_check_db_testmodel'


class HubAggregators(models.Model):
    aggregator = models.ForeignKey(Aggregators, models.DO_NOTHING, unique=True)
    hub = models.ForeignKey('Hubs', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hub_aggregators'


class HubTypes(models.Model):
    type = models.CharField(max_length=15)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hub_types'


class HubVillages(models.Model):
    hub = models.ForeignKey('Hubs', models.DO_NOTHING)
    village = models.ForeignKey('Locations', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'hub_villages'


class Hubs(models.Model):
    supplier_ptr = models.ForeignKey('Suppliers', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=15)
    hub_type = models.ForeignKey(HubTypes, models.DO_NOTHING)
    joining_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hubs'


class ImplementBrandTypeMapping(models.Model):
    brand = models.ForeignKey('ImplementBrands', models.DO_NOTHING)
    type = models.ForeignKey('ImplementTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'implement_brand_type_mapping'


class ImplementBrands(models.Model):
    name = models.CharField(max_length=40)
    resource_key = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'implement_brands'


class ImplementSku(models.Model):
    brand = models.ForeignKey(ImplementBrands, models.DO_NOTHING)
    sku = models.ForeignKey('Sku', models.DO_NOTHING, unique=True)
    spec = models.ForeignKey('ImplementSpecs', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('ImplementTypes', models.DO_NOTHING)
    model = models.CharField(max_length=30, blank=True, null=True)
    pricing_model = models.ForeignKey('PricingModels', models.DO_NOTHING, blank=True, null=True)
    soil_condition = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'implement_sku'


class ImplementSpecs(models.Model):
    name = models.CharField(max_length=128)
    min_hp = models.IntegerField()
    max_hp = models.IntegerField()
    requires_auxiliary_valve = models.IntegerField()
    implement = models.ForeignKey('ImplementTypes', models.DO_NOTHING)
    resource_key = models.CharField(max_length=128)
    implement_image = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'implement_specs'


class ImplementTypes(models.Model):
    name = models.CharField(max_length=128)
    farming_stage = models.ForeignKey(FarmingStages, models.DO_NOTHING, blank=True, null=True)
    resource_key = models.CharField(max_length=128)
    implement_image = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    is_self_propelled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'implement_types'


class Locations(models.Model):
    name = models.CharField(max_length=30)
    country_code = models.CharField(max_length=3)
    state_code = models.CharField(max_length=5)
    code2001 = models.CharField(max_length=10)
    district_code = models.CharField(max_length=6)
    sub_district_code = models.CharField(max_length=8)
    village_code = models.CharField(unique=True, max_length=35)
    longitude = models.FloatField()
    latitude = models.FloatField()
    spatial_location = models.TextField(blank=True, null=True)  # This field type is a guess.
    locale = models.CharField(max_length=10, blank=True, null=True)
    complete_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class MeasurementUnits(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'measurement_units'


class OperatorSkills(models.Model):
    operator = models.ForeignKey('Operators', models.DO_NOTHING)
    skill = models.ForeignKey(ImplementTypes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'operator_skills'


class Operators(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    driving_license_number = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operators'


class OrderAssignedImplements(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    implement = models.ForeignKey('SupplierImplements', models.DO_NOTHING)
    order = models.ForeignKey('Orders', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_assigned_implements'
        unique_together = (('order', 'implement'),)


class OrderAssignedTractors(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    tractor = models.ForeignKey('SupplierTractors', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_assigned_tractors'
        unique_together = (('order', 'tractor'),)


class OrderAuditLogs(models.Model):
    event = models.CharField(max_length=128)
    juncture = models.DateTimeField()
    json = models.TextField()
    event_creator = models.ForeignKey('Users', models.DO_NOTHING)
    order = models.ForeignKey('Orders', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_audit_logs'


class OrderDesiredImplements(models.Model):
    metadata = models.CharField(max_length=500, blank=True, null=True)
    brand = models.ForeignKey(ImplementBrands, models.DO_NOTHING, blank=True, null=True)
    implement = models.ForeignKey(ImplementTypes, models.DO_NOTHING)
    implement_spec = models.ForeignKey(ImplementSpecs, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    desired_implement_sku = models.ForeignKey('Sku', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_desired_implements'


class OrderFeedback(models.Model):
    rating = models.PositiveIntegerField()
    comments = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField()
    added_by = models.ForeignKey('Users', models.DO_NOTHING)
    order = models.ForeignKey('Orders', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'order_feedback'


class OrderInvoices(models.Model):
    price_list = models.PositiveIntegerField()
    pricing_model = models.CharField(max_length=15)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    final_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    no_of_units = models.FloatField(blank=True, null=True)
    currency_type = models.CharField(max_length=30, blank=True, null=True)
    implement = models.ForeignKey(OrderDesiredImplements, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_invoices'


class OrderPayments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_on = models.DateTimeField()
    method = models.CharField(max_length=15)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    reasons = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_payments'


class OrderRejectionReasons(models.Model):
    reason = models.CharField(max_length=50)
    resource_key = models.CharField(max_length=55)

    class Meta:
        managed = False
        db_table = 'order_rejection_reasons'


class OrderRequests(models.Model):
    status = models.CharField(max_length=55, blank=True, null=True)
    sent_at = models.DateTimeField()
    response_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    aggregator = models.ForeignKey(Aggregators, models.DO_NOTHING)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    rejection_reason = models.ForeignKey(OrderRejectionReasons, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_requests'


class OrderRescheduleReasons(models.Model):
    reason = models.CharField(max_length=100)
    resource_key = models.CharField(max_length=100)
    reschedule_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'order_reschedule_reasons'


class OrderSuppliers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    distance = models.FloatField(blank=True, null=True)
    distance_unit = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'order_suppliers'
        unique_together = (('order', 'supplier'),)


class OrderTimelines(models.Model):
    paused_at = models.DateTimeField(blank=True, null=True)
    restarted_at = models.DateTimeField(blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_timelines'


class Orders(models.Model):
    status = models.CharField(max_length=50)
    placed_on = models.DateTimeField()
    scheduled_on = models.DateTimeField()
    duration = models.FloatField()
    duration_unit = models.CharField(max_length=15)
    work_started_at = models.DateTimeField(blank=True, null=True)
    work_ended_at = models.DateTimeField(blank=True, null=True)
    referrer = models.CharField(max_length=15)
    estimated_price = models.CharField(max_length=30)
    final_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    crop = models.ForeignKey(Crops, models.DO_NOTHING, blank=True, null=True)
    farm_land = models.ForeignKey(FarmLands, models.DO_NOTHING)
    farmer = models.ForeignKey(Farmers, models.DO_NOTHING)
    operator = models.ForeignKey(Operators, models.DO_NOTHING, blank=True, null=True)
    promotion = models.PositiveIntegerField(blank=True, null=True)
    operation_area_unit = models.ForeignKey(MeasurementUnits, models.DO_NOTHING, blank=True, null=True)
    operational_area = models.FloatField(blank=True, null=True)
    assignment_status = models.CharField(max_length=15)
    can_be_rescheduled = models.IntegerField()
    rescheduled_time = models.DateTimeField(blank=True, null=True)
    commission = models.FloatField()
    commission_rate = models.FloatField()
    actual_acrage = models.FloatField()
    order_source = models.CharField(max_length=20)
    booked_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    actual_scheduled_on = models.DateTimeField(blank=True, null=True)
    actual_duration = models.FloatField()
    calculated_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersOldorder(models.Model):
    old_order_id = models.CharField(max_length=20)
    order = models.ForeignKey(Orders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders_oldorder'


class OtpHotpHotpdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.IntegerField()
    key = models.CharField(max_length=80)
    digits = models.PositiveSmallIntegerField()
    tolerance = models.PositiveSmallIntegerField()
    counter = models.BigIntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'otp_hotp_hotpdevice'


class OtpStaticStaticdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'otp_static_staticdevice'


class OtpStaticStatictoken(models.Model):
    token = models.CharField(max_length=16)
    device = models.ForeignKey(OtpStaticStaticdevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'otp_static_statictoken'


class OtpTotpTotpdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.IntegerField()
    key = models.CharField(max_length=80)
    step = models.PositiveSmallIntegerField()
    t0 = models.BigIntegerField()
    digits = models.PositiveSmallIntegerField()
    tolerance = models.PositiveSmallIntegerField()
    drift = models.SmallIntegerField()
    last_t = models.BigIntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'otp_totp_totpdevice'


class PhoneNumbers(models.Model):
    phone_number = models.CharField(unique=True, max_length=15)
    is_active = models.IntegerField()
    type = models.CharField(max_length=15)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    is_primary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phone_numbers'


class PriceLists(models.Model):
    name = models.CharField(unique=True, max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.IntegerField()
    version = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'price_lists'


class PricingModels(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pricing_models'


class PromotionCampaignConstraints(models.Model):
    constraint = models.CharField(max_length=500)
    campaign = models.ForeignKey('PromotionCampaigns', models.DO_NOTHING)
    constraint_type = models.ForeignKey(CampaignConstraintTypes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotion_campaign_constraints'


class PromotionCampaignLocations(models.Model):
    campaign = models.ForeignKey('PromotionCampaigns', models.DO_NOTHING)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotion_campaign_locations'


class PromotionCampaigns(models.Model):
    name = models.CharField(unique=True, max_length=30)
    sms_template = models.TextField(blank=True, null=True)
    website_template = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    disclaimer = models.TextField(blank=True, null=True)
    discount = models.PositiveIntegerField()
    promotion_type = models.ForeignKey('PromotionTypes', models.DO_NOTHING)
    scheme = models.ForeignKey('PromotionSchemes', models.DO_NOTHING)
    vehicle = models.ForeignKey('PromotionVehicles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotion_campaigns'


class PromotionImages(models.Model):
    file = models.CharField(max_length=300)
    promotion = models.ForeignKey('Promotions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotion_images'


class PromotionSchemeConstraints(models.Model):
    constraint = models.CharField(max_length=500)
    campaign = models.ForeignKey(PromotionCampaigns, models.DO_NOTHING)
    constraint_type = models.ForeignKey('SchemeConstraintTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotion_scheme_constraints'


class PromotionSchemes(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'promotion_schemes'


class PromotionTypes(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'promotion_types'


class PromotionVehicleConstraints(models.Model):
    constraint = models.CharField(max_length=500)
    campaign = models.ForeignKey(PromotionCampaigns, models.DO_NOTHING)
    constraint_type = models.ForeignKey('VehicleConstraintTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'promotion_vehicle_constraints'


class PromotionVehicles(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'promotion_vehicles'


class Promotions(models.Model):
    code = models.CharField(max_length=30)
    prefix = models.CharField(max_length=10, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    campaign = models.ForeignKey(PromotionCampaigns, models.DO_NOTHING)
    generated_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'promotions'


class PushNotificationsApnsdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    registration_id = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    application_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_apnsdevice'


class PushNotificationsGcmdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.BigIntegerField(blank=True, null=True)
    registration_id = models.TextField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    cloud_message_type = models.CharField(max_length=3)
    application_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_gcmdevice'


class PushNotificationsWnsdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    registration_id = models.TextField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    application_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_wnsdevice'


class RegionPriceLists(models.Model):
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    price_list = models.ForeignKey(PriceLists, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_price_lists'


class SchemeConstraintTypes(models.Model):
    name = models.CharField(max_length=30)
    scheme = models.ForeignKey(PromotionSchemes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scheme_constraint_types'


class SendPushNotificationsAggregatordevice(models.Model):
    aggregator = models.ForeignKey(Aggregators, models.DO_NOTHING)
    fcm_device = models.ForeignKey(PushNotificationsGcmdevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'send_push_notifications_aggregatordevice'


class SendPushNotificationsFarmerdevice(models.Model):
    farmer = models.ForeignKey(Farmers, models.DO_NOTHING)
    fcm_device = models.ForeignKey(PushNotificationsGcmdevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'send_push_notifications_farmerdevice'


class SendPushNotificationsNotification(models.Model):
    object_type = models.CharField(max_length=15)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    app_type = models.CharField(max_length=15)
    created_date = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    expired_at = models.DateTimeField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'send_push_notifications_notification'


class SendPushNotificationsSupplierheaddevice(models.Model):
    fcm_device = models.ForeignKey(PushNotificationsGcmdevice, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'send_push_notifications_supplierheaddevice'


class SendPushNotificationsSupplierownerdevice(models.Model):
    fcm_device = models.ForeignKey(PushNotificationsGcmdevice, models.DO_NOTHING)
    supplier_owner = models.ForeignKey('SupplierOwners', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'send_push_notifications_supplierownerdevice'


class ServiceLocations(models.Model):
    served_by_hub = models.IntegerField()
    served_by_aggregator = models.IntegerField()
    location = models.ForeignKey(Locations, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'service_locations'


class Sku(models.Model):
    sku = models.CharField(primary_key=True, max_length=36)
    sku_repr = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sku'


class SoilTypes(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'soil_types'


class StateCodes(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(unique=True, max_length=15)
    state_location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_codes'


class StateHeadLocationMapping(models.Model):
    created_at = models.DateTimeField()
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_head_location_mapping'


class StateLocations(models.Model):
    state_id = models.CharField(max_length=5)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_locations'


class SubTalukaLocations(models.Model):
    sub_taluka_id = models.CharField(max_length=5)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_taluka_locations'


class SupplierDriverAttributes(models.Model):
    driver_id = models.CharField(max_length=10)
    driver_code = models.CharField(max_length=10)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplier_driver_attributes'


class SupplierImplementImages(models.Model):
    file = models.CharField(max_length=100)
    implement = models.ForeignKey('SupplierImplements', models.DO_NOTHING)
    image_for = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_implement_images'


class SupplierImplements(models.Model):
    model_year = models.PositiveIntegerField()
    verification_status = models.CharField(max_length=15, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    brand = models.ForeignKey(ImplementBrands, models.DO_NOTHING, blank=True, null=True)
    spec = models.ForeignKey(ImplementSpecs, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(ImplementTypes, models.DO_NOTHING)
    model = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=36, blank=True, null=True)
    chassis = models.CharField(max_length=128, blank=True, null=True)
    is_deleted = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'supplier_implements'


class SupplierLocation(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    village = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplier_location'


class SupplierOperators(models.Model):
    operator = models.ForeignKey(Operators, models.DO_NOTHING, unique=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    is_permanent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier_operators'


class SupplierOwners(models.Model):
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplier_owners'


class SupplierTractorImages(models.Model):
    file = models.CharField(max_length=100)
    tractor = models.ForeignKey('SupplierTractors', models.DO_NOTHING)
    image_for = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_tractor_images'


class SupplierTractors(models.Model):
    license_plate_number = models.CharField(max_length=30, blank=True, null=True)
    year_of_manufacture = models.PositiveIntegerField()
    has_auxiliary_valve = models.IntegerField()
    verification_status = models.CharField(max_length=15, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    brand = models.ForeignKey('TractorBrands', models.DO_NOTHING)
    hp = models.PositiveIntegerField()
    model = models.CharField(max_length=30, blank=True, null=True)
    tyre_ballasting = models.IntegerField()
    name = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=36, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier_tractors'


class SupplierVillages(models.Model):
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    village = models.ForeignKey(Locations, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'supplier_villages'


class Suppliers(models.Model):
    supplier_type = models.CharField(max_length=15)
    commission = models.FloatField(blank=True, null=True)
    sap_entry_state = models.CharField(max_length=35)
    service_rating = models.FloatField(blank=True, null=True)
    supplier_code = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class SuppliersSupplierappinfo(models.Model):
    device_id = models.CharField(max_length=16)
    source = models.CharField(max_length=16)
    imei_number = models.CharField(max_length=16, blank=True, null=True)
    version = models.CharField(max_length=10)
    other = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Suppliers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'suppliers_supplierappinfo'


class SuppliersSupplierimplementcropmapping(models.Model):
    crop = models.ForeignKey(Crops, models.DO_NOTHING)
    supplier_implement = models.ForeignKey(SupplierImplements, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'suppliers_supplierimplementcropmapping'
        unique_together = (('supplier_implement', 'crop'),)


class TalukaLocations(models.Model):
    taluka_id = models.CharField(max_length=5)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taluka_locations'


class TractorBrands(models.Model):
    name = models.CharField(max_length=40)
    resource_key = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tractor_brands'


class TractorHps(models.Model):
    hp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tractor_hps'


class TractorImplementSku(models.Model):
    hp = models.PositiveIntegerField()
    implement_brand = models.ForeignKey(ImplementBrands, models.DO_NOTHING)
    implement_spec = models.ForeignKey(ImplementSpecs, models.DO_NOTHING)
    implement_type = models.ForeignKey(ImplementTypes, models.DO_NOTHING)
    sku = models.ForeignKey(Sku, models.DO_NOTHING, unique=True)
    tractor_brand = models.ForeignKey(TractorBrands, models.DO_NOTHING)
    has_aux_valve = models.IntegerField()
    implement_model = models.CharField(max_length=30, blank=True, null=True)
    tractor_model = models.CharField(max_length=30, blank=True, null=True)
    tyre_ballasting = models.IntegerField()
    pricing_model = models.ForeignKey(PricingModels, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tractor_implement_sku'


class TractorSku(models.Model):
    hp = models.PositiveIntegerField()
    brand = models.ForeignKey(TractorBrands, models.DO_NOTHING)
    sku = models.ForeignKey(Sku, models.DO_NOTHING, unique=True)
    has_aux_valve = models.IntegerField()
    model = models.CharField(max_length=30, blank=True, null=True)
    tyre_ballasting = models.IntegerField()
    pricing_model = models.ForeignKey(PricingModels, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tractor_sku'


class TwoFactorPhonedevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.IntegerField()
    number = models.CharField(max_length=128)
    key = models.CharField(max_length=40)
    method = models.CharField(max_length=4)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'two_factor_phonedevice'


class UserPreferences(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_preferences'
        unique_together = (('user', 'name'),)


class UserRoles(models.Model):
    group_ptr = models.ForeignKey(AuthGroup, models.DO_NOTHING, primary_key=True)
    alias_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=128, blank=True, null=True)
    profile_image = models.CharField(max_length=100, blank=True, null=True)
    reset_password = models.IntegerField()
    is_maintenance_staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('user', 'group'),)


class UsersUserPermissions(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_permissions'
        unique_together = (('user', 'permission'),)


class VehicleConstraintTypes(models.Model):
    name = models.CharField(max_length=30)
    vehicle = models.ForeignKey(PromotionVehicles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehicle_constraint_types'


class VillageLocations(models.Model):
    village_id = models.CharField(max_length=5)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'village_locations'
