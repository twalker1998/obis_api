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

class Comtax(models.Model):
    c_id           = models.IntegerField(primary_key=True)
    acode          = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.CASCADE)
    vernacularname = models.CharField(max_length=500, blank=True)
    primary_name   = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed  = False
        db_table = 'comtax'

class CoTrs(models.Model):
    gid  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    trs  = models.CharField(max_length=30, blank=True)
    geom = models.TextField(blank=True)

    class Meta:
        managed  = False
        db_table = 'co_trs'

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

class DistributionData(models.Model):
    d_id             = models.IntegerField(primary_key=True, blank=False, null=False)
    acode            = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.DO_NOTHING)
    elcode           = models.CharField(max_length=50, blank=True, null=True)
    origin           = models.ForeignKey('DOrigin', db_column='origin', blank=True, null=True, on_delete=models.DO_NOTHING)
    regularity       = models.ForeignKey('DRegularity', db_column='regularity', blank=True, null=True, on_delete=models.DO_NOTHING)
    dist_confidence  = models.ForeignKey(DDistConfidence, db_column='dist_confidence', blank=True, null=True, on_delete=models.DO_NOTHING)
    presence_absence = models.ForeignKey('DPresenceAbsence', db_column='presence_absence', blank=True, null=True, on_delete=models.DO_NOTHING)
    population       = models.ForeignKey('DPopulation', db_column='population', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        managed  = False
        db_table = 'distribution_data'

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

class NameCategoryDescLookup(models.Model):
    a_id               = models.IntegerField(blank=False, null=False)
    name_category_desc = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'name_category_desc_lu'

class NameTypeDescLookup(models.Model):
    a_id           = models.IntegerField(blank=False, null=False)
    name_type_desc = models.CharField(primary_key=True, max_length=30, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'name_type_desc_lu'

class NativityLookup(models.Model):
    n_id     = models.IntegerField(blank=False, null=False)
    nativity = models.CharField(primary_key=True, max_length=60, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'nativity_lu'

class Occurrence(models.Model):
    resourcetype                     = models.ForeignKey('ResourceTypeLookup', db_column='resourcetype', blank=True, null=True, on_delete=models.DO_NOTHING)
    gid                              = models.IntegerField(primary_key=True)
    acode                            = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.DO_NOTHING)
    eventdate                        = models.DateField(blank=True, null=True)
    recordedby                       = models.CharField(max_length=500, blank=True)
    county                           = models.ForeignKey(County, db_column='county', blank=True, null=True, on_delete=models.DO_NOTHING)
    locality                         = models.CharField(max_length=500, blank=True)
    behavior                         = models.CharField(max_length=500, blank=True)
    habitat                          = models.CharField(max_length=500, blank=True)
    sex                              = models.CharField(max_length=500, blank=True)
    lifestage                        = models.CharField(max_length=500, blank=True)
    associatedtaxa                   = models.CharField(max_length=500, blank=True)
    verbatimelevation                = models.FloatField(blank=True, null=True)
    depth                            = models.FloatField(blank=True, null=True)
    depthaccuracy                    = models.IntegerField(blank=True, null=True)
    individualcount                  = models.IntegerField(blank=True, null=True)
    occurrenceremarks                = models.CharField(max_length=500, blank=True)
    taxonremarks                     = models.CharField(max_length=500, blank=True)
    institutioncode                  = models.ForeignKey(Institution, db_column='institutioncode', blank=True, null=True, on_delete=models.CASCADE)
    basisofrecord                    = models.ForeignKey(BasisOfRecordLookup, db_column='basisofrecord', blank=True, null=True, on_delete=models.DO_NOTHING)
    catalognumber                    = models.CharField(max_length=500, blank=True)
    othercatalognumbers              = models.CharField(max_length=500, blank=True)
    typestatus                       = models.CharField(max_length=25, blank=True)
    recordnumber                     = models.CharField(max_length=500, blank=True)
    samplingprotocol                 = models.CharField(max_length=500, blank=True)
    preparations                     = models.CharField(max_length=500, blank=True)
    primary_data                     = models.CharField(max_length=500, blank=True)
    associatedreferences             = models.CharField(max_length=500, blank=True)
    datasetname                      = models.ForeignKey('Source', db_column='datasetname', blank=True, null=True, on_delete=models.DO_NOTHING)
    coordinateprecision              = models.IntegerField(blank=True, null=True)
    decimallatitude                  = models.FloatField(blank=True, null=True)
    decimallongitude                 = models.FloatField(blank=True, null=True)
    geodeticdatum                    = models.CharField(max_length=10, blank=True)
    georeferencedby                  = models.CharField(max_length=500, blank=True)
    georeferenceddate                = models.DateField(blank=True, null=True)
    georeferenceremarks              = models.CharField(max_length=500, blank=True)
    georeferencesources              = models.CharField(max_length=500, blank=True)
    georeferenceverificationstatus   = models.CharField(max_length=500, blank=True)
    geom                             = models.TextField(blank=True)
    problem_with_record              = models.CharField(max_length=500, blank=True)
    previousidentifications          = models.CharField(max_length=500, blank=True)
    identificationverificationstatus = models.CharField(max_length=500, blank=True)
    identificationconfidence         = models.CharField(max_length=10, blank=True)
    identificationremarks            = models.CharField(max_length=500, blank=True)
    datelastmodified                 = models.DateField(blank=True, null=True)
    associatedoccurrences            = models.CharField(max_length=500, blank=True)
    associatedsequences              = models.CharField(max_length=500, blank=True)
    entby                            = models.CharField(max_length=500, blank=True)
    entrydate                        = models.DateField(blank=True, null=True)
    obs_gid                          = models.IntegerField(blank=True, null=True)
    mtr                              = models.TextField(blank=True)
    township                         = models.IntegerField(blank=True, null=True)
    ns                               = models.TextField(blank=True)
    range                            = models.IntegerField(blank=True, null=True)
    ew                               = models.TextField(blank=True)
    section                          = models.IntegerField(blank=True, null=True)
    quarter                          = models.TextField(blank=True)
    zone                             = models.IntegerField(blank=True, null=True)
    utme                             = models.IntegerField(blank=True, null=True)
    utmn                             = models.IntegerField(blank=True, null=True)
    hiderecord                       = models.NullBooleanField()
    hiderecordcomment                = models.CharField(max_length=500, blank=True)
    relationshipremarks              = models.CharField(max_length=500, blank=True)
    informationwitheld               = models.NullBooleanField()
    awaitingreview                   = models.IntegerField(blank=True, null=True)
    occurrenceid                     = models.TextField(blank=True)

    class Meta:
        managed  = False
        db_table = 'occurrence'

class OkSwap(models.Model):
    swap_id     = models.IntegerField(primary_key=True)
    tier        = models.CharField(max_length=4, blank=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        managed  = False
        db_table = 'ok_swap'

class RankChange(models.Model):
    r_id                 = models.IntegerField(primary_key=True)
    acode                = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.DO_NOTHING)
    previous_s_rank      = models.CharField(max_length=500, blank=True)
    s_rank               = models.CharField(max_length=500, blank=True)
    changedby            = models.CharField(max_length=500, blank=True)
    rankremarks          = models.CharField(max_length=500, blank=True)
    datelastmodified     = models.DateField(blank=True, null=True)
    previousdatemodified = models.DateField(blank=True, null=True)

    class Meta:
        managed  = False
        db_table = 'rank_change'

class RasterColumns(models.Model):
    r_table_catalog  = models.TextField(blank=True)
    r_table_schema   = models.TextField(blank=True)
    r_table_name     = models.TextField(blank=True)
    r_raster_column  = models.TextField(blank=True)
    srid             = models.IntegerField(blank=True, null=True)
    scale_x          = models.FloatField(blank=True, null=True)
    scale_y          = models.FloatField(blank=True, null=True)
    blocksize_x      = models.IntegerField(blank=True, null=True)
    blocksize_y      = models.IntegerField(blank=True, null=True)
    same_alignment   = models.NullBooleanField()
    regular_blocking = models.NullBooleanField()
    num_bands        = models.IntegerField(blank=True, null=True)
    pixel_types      = models.TextField(blank=True)
    nodata_values    = models.TextField(blank=True)
    out_db           = models.TextField(blank=True)
    extent           = models.TextField(blank=True)

    class Meta:
        managed  = False
        db_table = 'raster_columns'

class RasterOverviews(models.Model):
    o_table_catalog = models.TextField(blank=True)
    o_table_schema  = models.TextField(blank=True)
    o_table_name    = models.TextField(blank=True)
    o_raster_column = models.TextField(blank=True)
    r_table_catalog = models.TextField(blank=True)
    r_table_schema  = models.TextField(blank=True)
    r_table_name    = models.TextField(blank=True)
    r_raster_column = models.TextField(blank=True)
    overview_factor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed  = False
        db_table = 'raster_overviews'

class ResourceTypeLookup(models.Model):
    id           = models.IntegerField(blank=False, null=False)
    resourcetype = models.CharField(primary_key=True, max_length=50, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'resourcetype_lu'

class Source(models.Model):
    source      = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        managed  = False
        db_table = 'source'

class SpatialRefSys(models.Model):
    srid      = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext    = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)

    class Meta:
        managed  = False
        db_table = 'spatial_ref_sys'

class StateRankLookup(models.Model):
    id   = models.IntegerField(blank=False, null=False)
    code = models.CharField(primary_key=True, max_length=15, blank=False, null=False)

    class Meta:
        managed  = False
        db_table = 'state_rank_lu'

class StStatus(models.Model):
    status_id   = models.IntegerField(primary_key=True)
    status      = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        managed  = False
        db_table = 'st_status'

class Syntax(models.Model):
    s_id                          = models.IntegerField()
    acode                         = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True, on_delete=models.CASCADE)
    scode                         = models.CharField(primary_key=True, max_length=500)
    sname                         = models.CharField(max_length=500, blank=True)
    scientificnameauthorship      = models.CharField(max_length=500, blank=True)
    family                        = models.CharField(max_length=500, blank=True)
    genus                         = models.CharField(max_length=500, blank=True)
    species                       = models.CharField(max_length=500, blank=True)
    subspecies                    = models.CharField(max_length=500, blank=True)
    variety                       = models.CharField(max_length=500, blank=True)
    scientificname                = models.CharField(max_length=500, blank=True)
    sspscientificnameauthorship   = models.CharField(max_length=500, blank=True)
    varscientificnameauthorship   = models.CharField(max_length=500, blank=True)
    formascientificnameauthorship = models.CharField(max_length=500, blank=True)
    tsn                           = models.IntegerField(blank=True, null=True)

    class Meta:
        managed  = False
        db_table = 'syntax'
