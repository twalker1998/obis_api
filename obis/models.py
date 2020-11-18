from __future__ import unicode_literals

from django.db import models

# TODO: comment / remove unused tables

class Acctax(models.Model):
    a_id                          = models.IntegerField(blank=True, null=True)
    acode                         = models.CharField(primary_key=True, max_length=500)
    sname                         = models.CharField(max_length=500, blank=True)
    scientificnameauthorship      = models.CharField(max_length=500, blank=True)
    family                        = models.ForeignKey('Hightax', db_column='family', blank=True, null=True, on_delete=models.CASCADE)
    genus                         = models.CharField(max_length=500, blank=True)
    species                       = models.CharField(max_length=500, blank=True)
    subspecies                    = models.CharField(max_length=500, blank=True)
    variety                       = models.CharField(max_length=500, blank=True)
    forma                         = models.CharField(max_length=500, blank=True)
    elcode                        = models.CharField(max_length=500, blank=True)
    gelcode                       = models.IntegerField(blank=True, null=True)
    iucncode                      = models.ForeignKey('IUCNLookup', db_column='iucncode', blank=True, null=True, on_delete=models.DO_NOTHING)
    g_rank                        = models.ForeignKey('GlobalRankLookup', db_column='g_rank', blank=True, null=True, on_delete=models.DO_NOTHING)
    s_rank                        = models.ForeignKey('StateRankLookup', db_column='s_rank', blank=True, null=True, on_delete=models.DO_NOTHING)
    nativity                      = models.ForeignKey('NativityLookup', db_column='nativity', blank=True, null=True, on_delete=models.CASCADE)
    source                        = models.CharField(max_length=500, blank=True)
    usda_code                     = models.CharField(max_length=500, blank=True)
    tsn                           = models.IntegerField(blank=True, null=True)
    fed_status                    = models.ForeignKey('FedStatus', blank=True, null=True, on_delete=models.DO_NOTHING)
    st_status                     = models.ForeignKey('StStatus', blank=True, null=True, on_delete=models.DO_NOTHING)
    swap                          = models.ForeignKey('OkSwap', blank=True, null=True, on_delete=models.DO_NOTHING)
    scientificname                = models.CharField(max_length=500, blank=True)
    sspscientificnameauthorship   = models.CharField(max_length=500, blank=True)
    varscientificnameauthorship   = models.CharField(max_length=500, blank=True)
    formascientificnameauthorship = models.CharField(max_length=500, blank=True)
    tracked                       = models.NullBooleanField() # TODO: remove NullBooleanField

    class Meta:
        managed  = False
        db_table = 'acctax'

class BasisOfRecordLookup(models.Model):
    id            = models.IntegerField(blank=False, null=False)
    basisofrecord = models.CharField(primary_key=True, max_length=50, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'basisofrecord_lu'

class CategoryLookup(models.Model):
    a_id     = models.IntegerField(blank=False, null=False)
    category = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'category_lu'

class CoTrs(models.Model):
    gid  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    trs  = models.CharField(max_length=30, blank=True)
    geom = models.TextField(blank=True)

    class Meta:
        managed  = False
        db_table = 'co_trs'

class Comtax(models.Model):
    c_id           = models.IntegerField(primary_key=True)
    acode          = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.CASCADE)
    vernacularname = models.CharField(max_length=500, blank=True)
    primary_name   = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed  = False
        db_table = 'comtax'

class County(models.Model):
    county = models.CharField(primary_key=True, unique=True, max_length=25, blank=True)
    gid    = models.IntegerField(blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'county'

class DDistConfidence(models.Model):
    d_dist_confidence_id = models.IntegerField(blank=False, null=False)
    dist_confidence      = models.CharField(primary_key=True, max_length=50, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'd_dist_confidence'

class DOrigin(models.Model):
    d_origin_id = models.IntegerField(blank=False, null=False)
    origin      = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'd_origin'

class DPopulation(models.Model):
    d_population_id = models.IntegerField(blank=False, null=False)
    population      = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'd_population'

class DPresenceAbsence(models.Model):
    d_presence_absence_id = models.IntegerField(blank=False, null=False)
    presence_absence      = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'd_presence_absence'

class DRegularity(models.Model):
    d_regularity_id = models.IntegerField(blank=False, null=False)
    regularity      = models.CharField(primary_key=True, max_length=50, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'd_regularity'

class DistributionData(models.Model):
    d_id             = models.IntegerField(primary_key=True, blank=False, null=False)
    acode            = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.DO_NOTHING)
    elcode           = models.CharField(max_length=50, blank=True, null=True)
    origin           = models.ForeignKey(DOrigin, db_column='origin', blank=True, null=True, on_delete=models.DO_NOTHING)
    regularity       = models.ForeignKey(DRegularity, db_column='regularity', blank=True, null=True, on_delete=models.DO_NOTHING)
    dist_confidence  = models.ForeignKey(DDistConfidence, db_column='dist_confidence', blank=True, null=True, on_delete=models.DO_NOTHING)
    presence_absence = models.ForeignKey(DPresenceAbsence, db_column='presence_absence', blank=True, null=True, on_delete=models.DO_NOTHING)
    population       = models.ForeignKey(DPopulation, db_column='population', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed  = False
        db_table = 'distribution_data'

class FedStatus(models.Model):
    status_id   = models.IntegerField(primary_key=True)
    status      = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        managed  = False
        db_table = 'fed_status'

class GeographyColumns(models.Model):
    f_table_catalog    = models.TextField(blank=True)
    f_table_schema     = models.TextField(blank=True)
    f_table_name       = models.TextField(blank=True)
    f_geography_column = models.TextField(blank=True)
    coord_dimension    = models.IntegerField(blank=True, null=True)
    srid               = models.IntegerField(blank=True, null=True)
    type               = models.TextField(blank=True)

    class Meta:
        managed  = False
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog   = models.CharField(max_length=256, blank=True)
    f_table_schema    = models.CharField(max_length=256, blank=True)
    f_table_name      = models.CharField(max_length=256, blank=True)
    f_geometry_column = models.CharField(max_length=256, blank=True)
    coord_dimension   = models.IntegerField(blank=True, null=True)
    srid              = models.IntegerField(blank=True, null=True)
    type              = models.CharField(max_length=30, blank=True)

    class Meta:
        managed  = False
        db_table = 'geometry_columns'

class GlobalRankLookup(models.Model):
    id = models.IntegerField(blank=False, null=False)
    code = models.CharField(primary_key=True, max_length=15, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'global_rank_lu'

class Hightax(models.Model):
    kingdom            = models.ForeignKey('KingdomLookup', db_column='kingdom', blank=False, null=False, on_delete=models.DO_NOTHING) # TODO: this might not work
    phylum             = models.CharField(max_length=500, blank=True)
    taxclass           = models.CharField(max_length=500, blank=True)
    taxorder           = models.CharField(max_length=500, blank=True)
    family             = models.CharField(primary_key=True, max_length=500)
    category           = models.ForeignKey('CategoryLookup', db_column='category', blank=True, null=True, on_delete=models.DO_NOTHING)
    name_type_desc     = models.ForeignKey('NameTypeDescLookup', db_column='name_type_desc', blank=True, null=True, on_delete=models.DO_NOTHING)
    name_category_desc = models.ForeignKey('NameCategoryDescLookup', db_column='name_category_desc', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed  = False
        db_table = 'hightax'

class IdentificationVerification(models.Model):
    pkey                  = models.IntegerField(primary_key=True)
    catalognumber         = models.CharField(max_length=500, blank=True)
    identifiedby          = models.CharField(max_length=500, blank=True)
    identificationremarks = models.CharField(max_length=500, blank=True)
    datalastmodified      = models.CharField(max_length=500, blank=True)
    identifiedacode       = models.CharField(max_length=500, blank=True)
    gid                   = models.ForeignKey('Occurrence', db_column='gid', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed  = False
        db_table = 'identification_verification'

class Institution(models.Model):
    institutioncode = models.CharField(primary_key=True, max_length=10)
    institution     = models.CharField(max_length=75, blank=True)
    curator         = models.CharField(max_length=25, blank=True)
    email           = models.CharField(max_length=40, blank=True)
    telephone       = models.CharField(max_length=100, blank=True)
    address         = models.CharField(max_length=100, blank=True)
    city            = models.CharField(max_length=20, blank=True)
    state           = models.CharField(max_length=2, blank=True)
    country         = models.CharField(max_length=5, blank=True)
    zipcode         = models.CharField(max_length=55, blank=True)
    institutiontype = models.CharField(max_length=50, blank=True)
    link            = models.CharField(max_length=500, blank=True) # TODO: what is this?

    class Meta:
        managed  = False
        db_table = 'institution'

class IUCNLookup(models.Model):
    code        = models.CharField(primary_key=True, max_length=2, blank=False, null=False)
    description = models.CharField(max_length=60, blank=False, null=False)
    id          = models.IntegerField(blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'iucn_lu'

class KingdomLookup(models.Model):
    id      = models.IntegerField(blank=False, null=False)
    kingdom = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'kingdom_lu'
