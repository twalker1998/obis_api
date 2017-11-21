# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class SearchView(models.Model):
    a_id = models.IntegerField()
    acc = models.CharField(primary_key=True, max_length=255)
    acode = models.CharField(max_length=255,blank=False)
    sname = models.CharField(max_length=255, blank=True)
    scientificnameauthorship = models.CharField(max_length=255, blank=True)
    kingdom = models.CharField(max_length=255, blank=True)
    phylum = models.CharField(max_length=255, blank=True)
    taxclass = models.CharField(max_length=255, blank=True)
    taxorder = models.CharField(max_length=255, blank=True)
    family = models.CharField(max_length=255, blank=True)
    genus = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    subspecies = models.CharField(max_length=255, blank=True)
    variety = models.CharField(max_length=255, blank=True)
    forma = models.CharField(max_length=255, blank=True)
    elcode = models.CharField(max_length=255, blank=True)
    gelcode = models.IntegerField(blank=True, null=True)
    iunccode = models.CharField(max_length=255, blank=True)
    g_rank = models.CharField(max_length=255, blank=True)
    s_rank = models.CharField(max_length=255, blank=True)
    nativity = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=255, blank=True)
    c_id = models.IntegerField()
    vernacularname = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'search_view'
        ordering = ['acode']

class Acctax(models.Model):
    a_id = models.IntegerField()
    acode = models.CharField(primary_key=True, max_length=-1)
    sname = models.CharField(max_length=255, blank=True)
    scientificnameauthorship = models.CharField(max_length=255, blank=True)
    family = models.ForeignKey('Hightax', db_column='family', blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    subspecies = models.CharField(max_length=255, blank=True)
    variety = models.CharField(max_length=255, blank=True)
    forma = models.CharField(max_length=255, blank=True)
    elcode = models.CharField(max_length=255, blank=True)
    gelcode = models.IntegerField(blank=True, null=True)
    iucncode = models.CharField(max_length=255, blank=True)
    g_rank = models.CharField(max_length=255, blank=True)
    s_rank = models.CharField(max_length=255, blank=True)
    nativity = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=255, blank=True)
    usda_code = models.CharField(max_length=255, blank=True)
    itis_code = models.IntegerField(blank=True, null=True)
    fed_status = models.ForeignKey('FedStatus', blank=True, null=True)
    st_status = models.ForeignKey('StStatus', blank=True, null=True)
#    swap = models.ForeignKey('OkSwap', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    sspscientificnameauthorship = models.CharField(max_length=255, blank=True)
    varscientificnameauthorship = models.CharField(max_length=255, blank=True)
    formascientificnameauthorship = models.CharField(max_length=255, blank=True)
    tracked = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'acctax'


class Addr(models.Model):
    gid = models.IntegerField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fromhn = models.CharField(max_length=12, blank=True)
    tohn = models.CharField(max_length=12, blank=True)
    side = models.CharField(max_length=1, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    plus4 = models.CharField(max_length=4, blank=True)
    fromtyp = models.CharField(max_length=1, blank=True)
    totyp = models.CharField(max_length=1, blank=True)
    fromarmid = models.IntegerField(blank=True, null=True)
    toarmid = models.IntegerField(blank=True, null=True)
    arid = models.CharField(max_length=22, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    statefp = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'addr'


class Addrfeat(models.Model):
    gid = models.IntegerField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    statefp = models.CharField(max_length=2)
    aridl = models.CharField(max_length=22, blank=True)
    aridr = models.CharField(max_length=22, blank=True)
    linearid = models.CharField(max_length=22, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    lfromhn = models.CharField(max_length=12, blank=True)
    ltohn = models.CharField(max_length=12, blank=True)
    rfromhn = models.CharField(max_length=12, blank=True)
    rtohn = models.CharField(max_length=12, blank=True)
    zipl = models.CharField(max_length=5, blank=True)
    zipr = models.CharField(max_length=5, blank=True)
    edge_mtfcc = models.CharField(max_length=5, blank=True)
    parityl = models.CharField(max_length=1, blank=True)
    parityr = models.CharField(max_length=1, blank=True)
    plus4l = models.CharField(max_length=4, blank=True)
    plus4r = models.CharField(max_length=4, blank=True)
    lfromtyp = models.CharField(max_length=1, blank=True)
    ltotyp = models.CharField(max_length=1, blank=True)
    rfromtyp = models.CharField(max_length=1, blank=True)
    rtotyp = models.CharField(max_length=1, blank=True)
    offsetl = models.CharField(max_length=1, blank=True)
    offsetr = models.CharField(max_length=1, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'addrfeat'


class Bg(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    blkgrpce = models.CharField(max_length=1, blank=True)
    bg_id = models.CharField(primary_key=True, max_length=12)
    namelsad = models.CharField(max_length=13, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bg'


class Birds(models.Model):
    institutioncode = models.CharField(max_length=9, blank=True)
    county = models.CharField(max_length=25, blank=True)
    locality = models.CharField(max_length=60, blank=True)
    recordedby = models.CharField(max_length=60, blank=True)
    recordnumber = models.CharField(max_length=25, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    materialsampleid = models.CharField(max_length=40, blank=True)
    institutionid = models.CharField(max_length=40, blank=True)
    remarks = models.CharField(max_length=90, blank=True)
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    eventdate = models.DateField(blank=True, null=True)
    relationshipremarks = models.CharField(max_length=255, blank=True)
    decimallongitude = models.FloatField(blank=True, null=True)
    decimallatitude = models.FloatField(blank=True, null=True)
    coordinateprecision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'birds'


class CoTrs(models.Model):
    gid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    trs = models.CharField(max_length=30, blank=True)
    geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'co_trs'


class Comtax(models.Model):
    c_id = models.IntegerField(primary_key=True)
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    vernacularname = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'comtax'


class County(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    countyns = models.CharField(max_length=8, blank=True)
    cntyidfp = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=100, blank=True)
    namelsad = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    classfp = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    csafp = models.CharField(max_length=3, blank=True)
    cbsafp = models.CharField(max_length=5, blank=True)
    metdivfp = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'county'


class CountyLookup(models.Model):
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'county_lookup'


class CountysubLookup(models.Model):
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField()
    county = models.CharField(max_length=90, blank=True)
    cs_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'countysub_lookup'


class Cousub(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    cousubfp = models.CharField(max_length=5, blank=True)
    cousubns = models.CharField(max_length=8, blank=True)
    cosbidfp = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, blank=True)
    namelsad = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    classfp = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    cnectafp = models.CharField(max_length=3, blank=True)
    nectafp = models.CharField(max_length=5, blank=True)
    nctadvfp = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    awater = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cousub'


class DirectionLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=3, blank=True)

    class Meta:
        managed = False
        db_table = 'direction_lookup'


class Dokarrs(models.Model):
    institutioncode = models.CharField(max_length=7, blank=True)
    county = models.CharField(max_length=20, blank=True)
    locality = models.CharField(max_length=140, blank=True)
    recordedby = models.CharField(max_length=50, blank=True)
    recordnumber = models.CharField(max_length=25, blank=True)
    habitat = models.CharField(max_length=350, blank=True)
    remarks = models.CharField(max_length=350, blank=True)
    institutionid = models.CharField(max_length=100, blank=True)
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    eventdate = models.DateField(blank=True, null=True)
    relationshipremarks = models.CharField(max_length=255, blank=True)
    decimallongitude = models.FloatField(blank=True, null=True)
    decimallatitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dokarrs'


class Edges(models.Model):
    gid = models.IntegerField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    tfidl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tfidr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    smid = models.CharField(max_length=22, blank=True)
    lfromadd = models.CharField(max_length=12, blank=True)
    ltoadd = models.CharField(max_length=12, blank=True)
    rfromadd = models.CharField(max_length=12, blank=True)
    rtoadd = models.CharField(max_length=12, blank=True)
    zipl = models.CharField(max_length=5, blank=True)
    zipr = models.CharField(max_length=5, blank=True)
    featcat = models.CharField(max_length=1, blank=True)
    hydroflg = models.CharField(max_length=1, blank=True)
    railflg = models.CharField(max_length=1, blank=True)
    roadflg = models.CharField(max_length=1, blank=True)
    olfflg = models.CharField(max_length=1, blank=True)
    passflg = models.CharField(max_length=1, blank=True)
    divroad = models.CharField(max_length=1, blank=True)
    exttyp = models.CharField(max_length=1, blank=True)
    ttyp = models.CharField(max_length=1, blank=True)
    deckedroad = models.CharField(max_length=1, blank=True)
    artpath = models.CharField(max_length=1, blank=True)
    persist = models.CharField(max_length=1, blank=True)
    gcseflg = models.CharField(max_length=1, blank=True)
    offsetl = models.CharField(max_length=1, blank=True)
    offsetr = models.CharField(max_length=1, blank=True)
    tnidf = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tnidt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'edges'


class Eo(models.Model):
    eo_id = models.IntegerField(primary_key=True)
    first_obs_date = models.TextField(blank=True)
    last_obs_date = models.TextField(blank=True)
    eo_data = models.CharField(max_length=255, blank=True)
    size_of_eo = models.IntegerField(blank=True, null=True)
    d_basic_eo_rank_id = models.IntegerField(blank=True, null=True)
    eo_rank_date = models.DateField(blank=True, null=True)
    eo_rank_com = models.CharField(max_length=255, blank=True)
    gen_desc = models.CharField(max_length=255, blank=True)
    gen_com = models.CharField(max_length=255, blank=True)
    survey_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eo'


class Faces(models.Model):
    gid = models.IntegerField(primary_key=True)
    tfid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    statefp00 = models.CharField(max_length=2, blank=True)
    countyfp00 = models.CharField(max_length=3, blank=True)
    tractce00 = models.CharField(max_length=6, blank=True)
    blkgrpce00 = models.CharField(max_length=1, blank=True)
    blockce00 = models.CharField(max_length=4, blank=True)
    cousubfp00 = models.CharField(max_length=5, blank=True)
    submcdfp00 = models.CharField(max_length=5, blank=True)
    conctyfp00 = models.CharField(max_length=5, blank=True)
    placefp00 = models.CharField(max_length=5, blank=True)
    aiannhfp00 = models.CharField(max_length=5, blank=True)
    aiannhce00 = models.CharField(max_length=4, blank=True)
    comptyp00 = models.CharField(max_length=1, blank=True)
    trsubfp00 = models.CharField(max_length=5, blank=True)
    trsubce00 = models.CharField(max_length=3, blank=True)
    anrcfp00 = models.CharField(max_length=5, blank=True)
    elsdlea00 = models.CharField(max_length=5, blank=True)
    scsdlea00 = models.CharField(max_length=5, blank=True)
    unsdlea00 = models.CharField(max_length=5, blank=True)
    uace00 = models.CharField(max_length=5, blank=True)
    cd108fp = models.CharField(max_length=2, blank=True)
    sldust00 = models.CharField(max_length=3, blank=True)
    sldlst00 = models.CharField(max_length=3, blank=True)
    vtdst00 = models.CharField(max_length=6, blank=True)
    zcta5ce00 = models.CharField(max_length=5, blank=True)
    tazce00 = models.CharField(max_length=6, blank=True)
    ugace00 = models.CharField(max_length=5, blank=True)
    puma5ce00 = models.CharField(max_length=5, blank=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    blkgrpce = models.CharField(max_length=1, blank=True)
    blockce = models.CharField(max_length=4, blank=True)
    cousubfp = models.CharField(max_length=5, blank=True)
    submcdfp = models.CharField(max_length=5, blank=True)
    conctyfp = models.CharField(max_length=5, blank=True)
    placefp = models.CharField(max_length=5, blank=True)
    aiannhfp = models.CharField(max_length=5, blank=True)
    aiannhce = models.CharField(max_length=4, blank=True)
    comptyp = models.CharField(max_length=1, blank=True)
    trsubfp = models.CharField(max_length=5, blank=True)
    trsubce = models.CharField(max_length=3, blank=True)
    anrcfp = models.CharField(max_length=5, blank=True)
    ttractce = models.CharField(max_length=6, blank=True)
    tblkgpce = models.CharField(max_length=1, blank=True)
    elsdlea = models.CharField(max_length=5, blank=True)
    scsdlea = models.CharField(max_length=5, blank=True)
    unsdlea = models.CharField(max_length=5, blank=True)
    uace = models.CharField(max_length=5, blank=True)
    cd111fp = models.CharField(max_length=2, blank=True)
    sldust = models.CharField(max_length=3, blank=True)
    sldlst = models.CharField(max_length=3, blank=True)
    vtdst = models.CharField(max_length=6, blank=True)
    zcta5ce = models.CharField(max_length=5, blank=True)
    tazce = models.CharField(max_length=6, blank=True)
    ugace = models.CharField(max_length=5, blank=True)
    puma5ce = models.CharField(max_length=5, blank=True)
    csafp = models.CharField(max_length=3, blank=True)
    cbsafp = models.CharField(max_length=5, blank=True)
    metdivfp = models.CharField(max_length=5, blank=True)
    cnectafp = models.CharField(max_length=3, blank=True)
    nectafp = models.CharField(max_length=5, blank=True)
    nctadvfp = models.CharField(max_length=5, blank=True)
    lwflag = models.CharField(max_length=1, blank=True)
    offset = models.CharField(max_length=1, blank=True)
    atotal = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'faces'


class Featnames(models.Model):
    gid = models.IntegerField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    predirabrv = models.CharField(max_length=15, blank=True)
    pretypabrv = models.CharField(max_length=50, blank=True)
    prequalabr = models.CharField(max_length=15, blank=True)
    sufdirabrv = models.CharField(max_length=15, blank=True)
    suftypabrv = models.CharField(max_length=50, blank=True)
    sufqualabr = models.CharField(max_length=15, blank=True)
    predir = models.CharField(max_length=2, blank=True)
    pretyp = models.CharField(max_length=3, blank=True)
    prequal = models.CharField(max_length=2, blank=True)
    sufdir = models.CharField(max_length=2, blank=True)
    suftyp = models.CharField(max_length=3, blank=True)
    sufqual = models.CharField(max_length=2, blank=True)
    linearid = models.CharField(max_length=22, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    paflag = models.CharField(max_length=1, blank=True)
    statefp = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'featnames'


class FedStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'fed_status'


class Fish(models.Model):
    recordnumber = models.CharField(max_length=254, blank=True)
    locality = models.CharField(max_length=254, blank=True)
    habitat = models.CharField(max_length=254, blank=True)
    decimallatitude = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    decimallongitude = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    recordedby = models.CharField(max_length=254, blank=True)
    permitnumber = models.CharField(max_length=254, blank=True)
    remarks = models.CharField(max_length=254, blank=True)
    institutioncode = models.CharField(max_length=254, blank=True)
    entryby = models.CharField(db_column='entryBy', max_length=254, blank=True)  # Field name made lowercase.
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    instutionid = models.CharField(max_length=3, blank=True)
    eventdate = models.DateField(blank=True, null=True)
    gid = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fish'


class GeocodeSettings(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True)
    unit = models.TextField(blank=True)
    category = models.TextField(blank=True)
    short_desc = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings'


class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    f_table_schema = models.TextField(blank=True)  # This field type is a guess.
    f_table_name = models.TextField(blank=True)  # This field type is a guess.
    f_geography_column = models.TextField(blank=True)  # This field type is a guess.
    coord_dimension = models.IntegerField(blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'geography_columns'


class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256, blank=True)
    f_table_schema = models.CharField(max_length=256, blank=True)
    f_table_name = models.CharField(max_length=256, blank=True)
    f_geometry_column = models.CharField(max_length=256, blank=True)
    coord_dimension = models.IntegerField(blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'geometry_columns'


class Herbaria(models.Model):
    institutioncode = models.CharField(primary_key=True, max_length=10)
    institution = models.CharField(max_length=75, blank=True)
    curator = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=40, blank=True)
    telephone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)

    class Meta:
        managed = False
        db_table = 'herbaria'


class Hightax(models.Model):
    kingdom = models.CharField(max_length=255, blank=True)
    phylum = models.CharField(max_length=255, blank=True)
    taxclass = models.CharField(max_length=255, blank=True)
    taxorder = models.CharField(max_length=255, blank=True)
    family = models.CharField(primary_key=True, max_length=-1)
    category = models.CharField(max_length=255, blank=True)
    name_type_desc = models.CharField(max_length=255, blank=True)
    name_category_desc = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'hightax'


class Layer(models.Model):
    topology = models.ForeignKey('Topology')
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=255)
    table_name = models.CharField(max_length=255)
    feature_column = models.CharField(max_length=255)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'


class LoaderLookuptables(models.Model):
    process_order = models.IntegerField()
    lookup_name = models.TextField(primary_key=True)
    table_name = models.TextField(blank=True)
    single_mode = models.BooleanField()
    load = models.BooleanField()
    level_county = models.BooleanField()
    level_state = models.BooleanField()
    level_nation = models.BooleanField()
    post_load_process = models.TextField(blank=True)
    single_geom_mode = models.NullBooleanField()
    insert_mode = models.CharField(max_length=1)
    pre_load_process = models.TextField(blank=True)
    columns_exclude = models.TextField(blank=True)  # This field type is a guess.
    website_root_override = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'loader_lookuptables'


class LoaderPlatform(models.Model):
    os = models.CharField(primary_key=True, max_length=50)
    declare_sect = models.TextField(blank=True)
    pgbin = models.TextField(blank=True)
    wget = models.TextField(blank=True)
    unzip_command = models.TextField(blank=True)
    psql = models.TextField(blank=True)
    path_sep = models.TextField(blank=True)
    loader = models.TextField(blank=True)
    environ_set_command = models.TextField(blank=True)
    county_process_command = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'loader_platform'


class LoaderVariables(models.Model):
    tiger_year = models.CharField(primary_key=True, max_length=4)
    website_root = models.TextField(blank=True)
    staging_fold = models.TextField(blank=True)
    data_schema = models.TextField(blank=True)
    staging_schema = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'loader_variables'


class Mammals(models.Model):
    institutioncode = models.CharField(max_length=25, blank=True)
    county = models.CharField(max_length=15, blank=True)
    locality = models.CharField(max_length=105, blank=True)
    recordedby = models.CharField(max_length=60, blank=True)
    recordnumber = models.CharField(max_length=15, blank=True)
    sex = models.CharField(max_length=12, blank=True)
    materialsampleid = models.CharField(max_length=45, blank=True)
    institutionid = models.CharField(max_length=45, blank=True)
    relationshipremarks = models.CharField(max_length=255, blank=True)
    eventdate = models.DateField(db_column='eventDate', blank=True, null=True)  # Field name made lowercase.
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    decimallongitude = models.FloatField(blank=True, null=True)
    decimallatitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mammals'


class NameCat(models.Model):
    d_name_category_id = models.IntegerField(primary_key=True)
    name_type_desc = models.CharField(max_length=255, blank=True)
    name_category_desc = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'name_cat'


class Observation(models.Model):
    source_feature_descriptor = models.CharField(max_length=255, blank=True)
    source_feature_locator = models.CharField(max_length=255, blank=True)
    coordinateprecision = models.IntegerField(blank=True, null=True)
    georeferencesources = models.CharField(max_length=255, blank=True)
    recordedby = models.CharField(max_length=255, blank=True)
    eventdate = models.DateField(blank=True, null=True)
    occurrenceremarks = models.CharField(max_length=255, blank=True)
    eo_id = models.IntegerField(blank=True, null=True)
    locationremarks = models.CharField(max_length=255, blank=True)
    decimallongitude = models.FloatField(blank=True, null=True)
    decimallatitude = models.FloatField(blank=True, null=True)
    gid = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True)  # This field type is a guess.
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observation'


class OkSwap(models.Model):
    swap_id = models.IntegerField(primary_key=True)
    tier = models.CharField(max_length=4, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'ok_swap'


class OvpdAnnotation(models.Model):
    pkey = models.IntegerField(blank=True, null=True)
    accno = models.TextField(blank=True)
    annotsymbol = models.TextField(blank=True)
    annotator = models.TextField(blank=True)
    anndate = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    annotacode = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'ovpd_annotation'


class OvpdLocation(models.Model):
    instutitionid = models.ForeignKey(Herbaria, db_column='instutitionid', blank=True, null=True)
    institutioncode = models.TextField(blank=True)
    symbol = models.TextField(blank=True)
    identificationverificationstatus = models.TextField(blank=True)
    collidsymbol = models.TextField(blank=True)
    recordedby = models.TextField(blank=True)
    recordnumber = models.TextField(blank=True)
    eventdate = models.DateField(blank=True, null=True)
    otherdate = models.TextField(blank=True)
    county = models.TextField(blank=True)
    mtr = models.TextField(blank=True)
    trsproblem = models.TextField(blank=True)
    trsattrib = models.TextField(blank=True)
    township = models.IntegerField(blank=True, null=True)
    ns = models.TextField(blank=True)
    range = models.IntegerField(blank=True, null=True)
    ew = models.TextField(blank=True)
    section = models.IntegerField(blank=True, null=True)
    quarter = models.TextField(blank=True)
    zone = models.IntegerField(blank=True, null=True)
    utme = models.IntegerField(blank=True, null=True)
    utmn = models.IntegerField(blank=True, null=True)
    locality = models.TextField(blank=True)
    habitat = models.TextField(blank=True)
    organismremarks = models.TextField(blank=True)
    associatedorganisms = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    cultivated = models.SmallIntegerField(blank=True, null=True)
    cultivatedcomments = models.TextField(blank=True)
    entby = models.TextField(blank=True)
    entrydate = models.CharField(max_length=29, blank=True)
    mark = models.TextField(blank=True)
    qccomp = models.TextField(blank=True)
    heritagehas = models.TextField(blank=True)
    hiderecord = models.SmallIntegerField(blank=True, null=True)
    hiderecordcomment = models.TextField(blank=True)
    awaitingreview = models.SmallIntegerField(blank=True, null=True)
    acode = models.TextField(blank=True)
    collidacode = models.CharField(max_length=20, blank=True)
    decimallongitude = models.FloatField(blank=True, null=True)
    decimallatitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ovpd_location'


class PagcGaz(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True)
    stdword = models.TextField(blank=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_gaz'


class PagcLex(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True)
    stdword = models.TextField(blank=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_lex'


class PagcRules(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    rule = models.TextField(blank=True)
    is_custom = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_rules'


class Place(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True)
    placefp = models.CharField(max_length=5, blank=True)
    placens = models.CharField(max_length=8, blank=True)
    plcidfp = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=100, blank=True)
    namelsad = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    classfp = models.CharField(max_length=2, blank=True)
    cpi = models.CharField(max_length=1, blank=True)
    pcicbsa = models.CharField(max_length=1, blank=True)
    pcinecta = models.CharField(max_length=1, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'place'


class PlaceLookup(models.Model):
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True)
    pl_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True)

    class Meta:
        managed = False
        db_table = 'place_lookup'


class RasterColumns(models.Model):
    r_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    r_table_schema = models.TextField(blank=True)  # This field type is a guess.
    r_table_name = models.TextField(blank=True)  # This field type is a guess.
    r_raster_column = models.TextField(blank=True)  # This field type is a guess.
    srid = models.IntegerField(blank=True, null=True)
    scale_x = models.FloatField(blank=True, null=True)
    scale_y = models.FloatField(blank=True, null=True)
    blocksize_x = models.IntegerField(blank=True, null=True)
    blocksize_y = models.IntegerField(blank=True, null=True)
    same_alignment = models.NullBooleanField()
    regular_blocking = models.NullBooleanField()
    num_bands = models.IntegerField(blank=True, null=True)
    pixel_types = models.TextField(blank=True)  # This field type is a guess.
    nodata_values = models.TextField(blank=True)  # This field type is a guess.
    out_db = models.TextField(blank=True)  # This field type is a guess.
    extent = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'raster_columns'


class RasterOverviews(models.Model):
    o_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    o_table_schema = models.TextField(blank=True)  # This field type is a guess.
    o_table_name = models.TextField(blank=True)  # This field type is a guess.
    o_raster_column = models.TextField(blank=True)  # This field type is a guess.
    r_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    r_table_schema = models.TextField(blank=True)  # This field type is a guess.
    r_table_name = models.TextField(blank=True)  # This field type is a guess.
    r_raster_column = models.TextField(blank=True)  # This field type is a guess.
    overview_factor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raster_overviews'


class SecondaryUnitLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=5, blank=True)

    class Meta:
        managed = False
        db_table = 'secondary_unit_lookup'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class StStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'st_status'


class State(models.Model):
    gid = models.IntegerField(unique=True)
    region = models.CharField(max_length=2, blank=True)
    division = models.CharField(max_length=2, blank=True)
    statefp = models.CharField(primary_key=True, max_length=2)
    statens = models.CharField(max_length=8, blank=True)
    stusps = models.CharField(unique=True, max_length=2)
    name = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'state'


class StateLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, blank=True)
    abbrev = models.CharField(unique=True, max_length=3, blank=True)
    statefp = models.CharField(unique=True, max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'state_lookup'


class StreetTypeLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    abbrev = models.CharField(max_length=50, blank=True)
    is_hw = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'street_type_lookup'


class SurveySite(models.Model):
    eo_id = models.IntegerField(blank=True, null=True)
    survey_site_name = models.CharField(max_length=255, blank=True)
    survey_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'survey_site'


class Syntax(models.Model):
    s_id = models.IntegerField()
    acode = models.ForeignKey(Acctax, db_column='acode', blank=True, null=True)
    scode = models.CharField(primary_key=True, max_length=-1)
    sname = models.CharField(max_length=255, blank=True)
    scientificnameauthorship = models.CharField(max_length=255, blank=True)
    family = models.CharField(max_length=255, blank=True)
    genus = models.CharField(max_length=255, blank=True)
    species = models.CharField(max_length=255, blank=True)
    subspecies = models.CharField(max_length=255, blank=True)
    variety = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    sspscientificnameauthorship = models.CharField(max_length=255, blank=True)
    varscientificnameauthorship = models.CharField(max_length=255, blank=True)
    formascientificnameauthorship = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'syntax'


class Tabblock(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    blockce = models.CharField(max_length=4, blank=True)
    tabblock_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=20, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    ur = models.CharField(max_length=1, blank=True)
    uace = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tabblock'


class Topology(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'


class Tract(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    tract_id = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=7, blank=True)
    namelsad = models.CharField(max_length=20, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tract'


class VwAllTaxa(models.Model):
    unique_code = models.CharField(max_length=255, blank=True)
    sname = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    status = models.TextField(blank=True)
    accepted_code = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'vw_all_taxa'


class VwSpatialAttribute(models.Model):
    name = models.CharField(max_length=100, blank=True)
    trs = models.CharField(max_length=30, blank=True)
    gid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_spatial_attribute'


class VwTracked(models.Model):
    family = models.CharField(max_length=255, blank=True)
    sname = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    s_rank = models.CharField(max_length=255, blank=True)
    g_rank = models.CharField(max_length=255, blank=True)
    name_type_desc = models.CharField(max_length=255, blank=True)
    name_category_desc = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'vw_tracked'


class VwUniqueAcodeScode(models.Model):
    unique_code = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'vw_unique_acode_scode'


class Zcta5(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2)
    zcta5ce = models.CharField(max_length=5)
    classfp = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    partflg = models.CharField(max_length=1, blank=True)
    the_geom = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'zcta5'


class ZipLookup(models.Model):
    zip = models.IntegerField(primary_key=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup'


class ZipLookupAll(models.Model):
    zip = models.IntegerField(blank=True, null=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_all'


class ZipLookupBase(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    state = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=90, blank=True)
    city = models.CharField(max_length=90, blank=True)
    statefp = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_base'


class ZipState(models.Model):
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = False
        db_table = 'zip_state'


class ZipStateLoc(models.Model):
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True)
    place = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'zip_state_loc'
