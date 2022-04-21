    # a =  {
    #                     "deleted_at": "null",
    #                     "nomor_kasus": "0938300521-8304-L",
    #                     "tanggal_kejadian": "2005-01-18",
    #                     "tanggal_teridentifikasi": "2003-01-18",
    #                     "tanggal_input": "1971-08-21",
    #                     "tanggal_selesai": "1983-06-30",
    #                     "tanggal_update": "2008-02-18T12:53:26Z",
    #                     "jumlah_kasus": 5298,
    #                     "nama_pembuat": "Doganti nilai tukar",
    #                     "status": "As computer floor door pay up enter.",
    #                     "kode_cabang": 7,
    #                     "kode_produk": 14,
    #                     "nama_penemu": "Their meeting wife operation.\\nSince road society official government gas.",
    #                     "kode_ktg_kejadian": "Place gun to light.",
    #                     "kode_penyebab": "Grow keep site.",
    #                     "coa_biaya": 700000,
    #                     "mata_uang": "Drug.",
    #                     "nilai_tukar": 13919,
    #                     "kerugian_potensial": -5897378318697373138,
    #                     "rra": 6328708944106519179,
    #                     "recovery": -6385607385267134766,
    #                     "kerugian_aktual": -824261160112919873,
    #                     "tanggal_review": "2014-01-04",
    #                     "reviewer": "Window meet course.",
    #                     "hasil_review": "Member range magazine program. Question visit material attack camera. Society people bring become bad risk important.",
    #                     "keterangan_review": "Radio common head carry director people either. Financial nor person seem wrong TV do contain. Item or memory else.\\nSecurity machine real return her may company. School side cut.",
    #                     "summary_kejadian": "Listen serve he which among art. Present dinner program join fall enjoy.\\nModel explain condition expect. Outside near professor finish seven she.",
    #                     "kronologi_kejadian": "Thought policy difficult face. Participant paper ten sell. Break my debate standard experience discuss eat foreign.",
    #                     "tindakan_unit_kerja": "Instead attack city floor language interest. Kid authority of face method.\\nSpend need only soldier light. Together choose hotel clearly fire put gas. Nation central picture each play oil their.",
    #                     "tindakan_perbaikan": "Discover federal window hard compare blood fear. About conference over organization. Exactly seven although ago box black short upon.\\nNone between item simply. Eat energy explain.",
    #                     "dibuat_oleh": "Store quality recent under everything run travel. Raise table board able.",
    #                     "disetujui_oleh": "Total blood receive here recent south finish. Draw mission receive community true able.",
    #                     "risiko_kredit": "Her describe.",
    #                     "created_at": "2004-06-27T19:13:23Z",
    #                     "updated_at": "2004-06-27T19:13:23Z"
    #                 }
    # b = {
    #                     "deleted_at": "null",
    #                     "nomor_kasus": "0938300521-8304-LL",
    #                     "tanggal_kejadian": "2005-01-18",
    #                     "tanggal_teridentifikasi": "2003-01-18",
    #                     "tanggal_input": "1971-08-21",
    #                     "tanggal_selesai": "1983-06-30",
    #                     "tanggal_update": "2008-02-18T12:53:26Z",
    #                     "jumlah_kasus": 5298,
    #                     "nama_pembuat": "Doganti nilai tukar",
    #                     "status": "As computer floor door pay up enter.",
    #                     "kode_cabang": 7,
    #                     "kode_produk": 14,
    #                     "nama_penemu": "Their meeting wife operation.\\nSince road society official government gas.",
    #                     "kode_ktg_kejadian": "Place gun to light.",
    #                     "kode_penyebab": "Grow keep site.",
    #                     "coa_biaya": 700000,
    #                     "mata_uang": "Drugs.",
    #                     "nilai_tukar": 13919,
    #                     "kerugian_potensial": -5897378318697373139,
    #                     "rra": 6328708944106519179,
    #                     "recovery": -6385607385267134766,
    #                     "kerugian_aktual": -824261160112919873,
    #                     "tanggal_review": "2014-01-04",
    #                     "reviewer": "Window meet course.",
    #                     "hasil_review": "Member range magazine program. Question visit material attack camera. Society people bring become bad risk important.",
    #                     "keterangan_review": "Radio common head carry director people either. Financial nor person seem wrong TV do contain. Item or memory else.\\nSecurity machine real return her may company. School side cut.",
    #                     "summary_kejadian": "Listen serve he which among art. Present dinner program join fall enjoy.\\nModel explain condition expect. Outside near professor finish seven she.",
    #                     "kronologi_kejadian": "Thought policy difficult face. Participant paper ten sell. Break my debate standard experience discuss eat foreign.",
    #                     "tindakan_unit_kerja": "Instead attack city floor language interest. Kid authority of face method.\\nSpend need only soldier light. Together choose hotel clearly fire put gas. Nation central picture each play oil their.",
    #                     "tindakan_perbaikan": "Discover federal window hard compare blood fear. About conference over organization. Exactly seven although ago box black short upon.\\nNone between item simply. Eat energy explain.",
    #                     "dibuat_oleh": "Store quality recent under everything run travel. Raise table board able.",
    #                     "disetujui_oleh": "Total blood receive here recent south finish. Draw mission receive community true able.",
    #                     "risiko_kredit": "Her describe.",
    #                     "created_at": "2004-06-27T19:13:23Z",
    #                     "updated_at": "2004-06-27T19:13:23Z"
    #                 }
       
   
    # a = serializers.serialize('json', [laporanBaru,])
    
    
    
    # b = serializers.serialize('json', [laporanBaru2,])
#     a = {
#        'number': 1,
#         'list': ['one', 'twox']
#    }

#     b = {
#        'list': ['one', 'two'],
#         'number': 2
#    }
    # count = 0
    # while (count < 2):
    #     # laporanBaru = Led.objects.get(id = 16)
    #     diff = DeepDiff(ledDict, ledDict2)
    #     diff2 = diff['values_changed']
    #     print(type(diff2))
    #     print(diff['values_changed'])
    #     count = count +1
        
        
    
    # for x in diff2:
    #     print (x)
    #     for y in diff2[x]:
    #         print (y,':',diff2[x][y])
            
    #     # count = count+1
    # path = "root['nomor_kasus']['new_value]"
    # print(diff2[0])
    # print(extract(diff2, path))
    # jsoned = diff.to_json()

    # print(json.dumps(jsoned, indent=4))

    # print(type(diff))
    
    
    <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Status</label>
                    <div class="form-group">
                        <input type="text" id="status" class='form-control' name="status" value='{{currLed.status}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Kode cabang</label>
                    <div class="form-group">

                        <select class="form-control select2 select2-hidden-accessible" name="kode_cabang"
                            style="height: 3em;" data-select2-id="1" tabindex="-1" aria-hidden="true">

                            <option selected>{{currLed.kode_cabang}}</option>
                            {% for cabang in kd_cabang %}
                            <option>{{cabang.nama_cabang}}</option>
                            {% endfor %}


                    </div>
                </div>
            </div>


           
               

            <div class="col-sm-3">
                <!-- textarea -->
                <label>Tanggal Kejadian</label>
                <div class="form-group">
                    <input type="date" id="date" class='form-control' name="tgl_kejadian"
                        value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>
                </div>
            </div>

#

{% extends "base.html"%}
{% block page-title %}
<h1> Edit LED </h1>
{% endblock page-title %}

{% block container-1 %}

<div class="card">
    <div class="card-header">
        <h3 class="card-title">Buat Laporan Baru</h3>
    </div>
    <!-- /.card-header -->
    <div class="card-body">
        <form role="form" method="POST">
            {% csrf_token %}
            <!-- text input -->

            <div class="form-group">
                <label>Nomor Kasus</label>
                <input type="text" class="form-control" placeholder="Judul" name="judul">
            </div>

            <div class="row">
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Kejadian</label>
                    <div class="form-group">
                        <input type="date" id="tgl_kejadian" class='form-control' name="tgl_kejadian"
                            value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>

                    </div>
                </div>
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Teridentifikasi</label>
                    <div class="form-group">
                        <input type="date" id="tgl_identifikasi" class='form-control' name="tgl_identifikasi"
                            value='{{currLed.tanggal_teridentifikasi| date:"Y-m-d"}}'>
                    </div>
                </div>
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Input</label>
                    <div class="form-group">
                        <input type="date" id="tgl_input" class='form-control' name="tgl_input"
                            value='{{currLed.tanggal_input| date:"Y-m-d"}}'>
                    </div>
                </div>

            </div>
            <div class="row">
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Selesai</label>
                    <div class="form-group">
                        <input type="date" id="tgl_selesai" class='form-control' name="tgl_selesai"
                            value='{{currLed.tanggal_selesai| date:"Y-m-d"}}'>
                    </div>
                </div>
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Update</label>
                    <div class="form-group">
                        <input type="date" id="tgl_update" class='form-control' name="tgl_update"
                            value='{{currLed.tanggal_update| date:"Y-m-d"}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Jumlah Kasus</label>
                    <div class="form-group">
                        <input type="text" id="jml_kasus" class='form-control' name="kml_kasus"
                            value='{{currLed.jumlah_kasus}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Tipe LED</label>
                    <div class="form-group">
                        <input type="text" id="tipe_led" class='form-control' name="tipe_led"
                            value='{{currLed.tipe_led}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Status</label>
                    <div class="form-group">
                        <input type="text" id="status" class='form-control' name="status" value='{{currLed.status}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Kode cabang</label>
                    <div class="">

                        <select class="form-control select2 select2-hidden-accessible" name="kode_cabang"
                            style="height: 3em;" data-select2-id="1" tabindex="-1" aria-hidden="true">

                            <option selected>{{currLed.kode_cabang}}</option>
                            {% for cabang in kd_cabang %}
                            <option>{{cabang.nama_cabang}}</option>
                            {% endfor %}


                    </div>
                </div>
            </div>


            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Kode produk</label>
                    <div class="form-group">
                        <input type="text" id="kode_produk" class='form-control' name="kode_produk"
                            value=>
                    </div>
                </div>
            </div>

            <div class="col-sm-3">
                <!-- textarea -->
                <label>Tanggal Kejadian</label>
                <div class="form-group">
                    <input type="date" id="date" class='form-control' name="tgl_kejadian"
                        value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>
                </div>
            </div>

            <div class="col-sm-3">
                <!-- textarea -->
                <label>Tanggal Kejadians</label>
                <div class="form-group">
                    <input type="date" id="date" class='form-control' name="tgl_kejadian"
                        value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>
                </div>
            </div>





            <div class="text-center">
                <button type="submit" class="btn btn-primary">Create</button>
            </div>

        </form>
    </div>
    <!-- /.card-body -->
</div>




{% endblock container-1 %}

##

{% extends "base.html"%} {% load static %}
{% block style-container %}
<!-- Select2 -->
<link rel="stylesheet" href="{% static 'plugins/select2/css/select2.min.css'%}">
<link rel="stylesheet" href="{% static 'plugins/select2-bootstrap4-theme/select2-bootstrap4.min.css' %}">
{% endblock style-container %}
{% block page-title %}
<h1> Edit LED </h1>
{% endblock page-title %}
{% block page-position %}
<li class="breadcrumb-item"><a href="#">LED Temporary</a></li>
<li class="breadcrumb-item"><a href="#">Review LED</a></li>
<li class="breadcrumb-item active">Edit LED</a></li>
{% endblock page-position %}

{% block container-1 %}

<div class="card">
    <div class="card-header">
        <h3 class="card-title">Buat Laporan Baru</h3>
    </div>
    <!-- /.card-header -->
    <div class="card-body">
        <form role="form" method="POST">
            {% csrf_token %}
            <!-- text input -->

            <div class="form-group">
                <label>Nomor Kasus</label>
                <input type="text" class="form-control" placeholder="Judul" name="judul">
            </div>

            <div class="row">
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Kejadian</label>
                    <div class="form-group">
                        <input type="date" id="tgl_kejadian" class='form-control' name="tgl_kejadian"
                            value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>

                    </div>
                </div>
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Teridentifikasi</label>
                    <div class="form-group">
                        <input type="date" id="tgl_identifikasi" class='form-control' name="tgl_identifikasi"
                            value='{{currLed.tanggal_teridentifikasi| date:"Y-m-d"}}'>
                    </div>
                </div>
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Input</label>
                    <div class="form-group">
                        <input type="date" id="tgl_input" class='form-control' name="tgl_input"
                            value='{{currLed.tanggal_input| date:"Y-m-d"}}'>
                    </div>
                </div>

            </div>
            <div class="row">
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Selesai</label>
                    <div class="form-group">
                        <input type="date" id="tgl_selesai" class='form-control' name="tgl_selesai"
                            value='{{currLed.tanggal_selesai| date:"Y-m-d"}}'>
                    </div>
                </div>
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Tanggal Update</label>
                    <div class="form-group">
                        <input type="date" id="tgl_update" class='form-control' name="tgl_update"
                            value='{{currLed.tanggal_update| date:"Y-m-d"}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-4">
                    <!-- textarea -->
                    <label>Jumlah Kasus</label>
                    <div class="form-group">
                        <input type="text" id="jml_kasus" class='form-control' name="kml_kasus"
                            value='{{currLed.jumlah_kasus}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Tipe LED</label>
                    <div class="form-group">
                        <input type="text" id="tipe_led" class='form-control' name="tipe_led"
                            value='{{currLed.tipe_led}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Status</label>
                    <div class="form-group">
                        <input type="text" id="status" class='form-control' name="status" value='{{currLed.status}}'>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Kode cabang</label>
                    <div class="">

                        <select class="form-control select2 select2-hidden-accessible" name="kode_cabang"
                            style="height: 3em;" data-select2-id="1" tabindex="-1" aria-hidden="true">

                            <option selected>{{currLed.kode_cabang}}</option>
                            {% for cabang in kd_cabang %}
                            <option>{{cabang.nama_cabang}}</option>
                            {% endfor %}
                    </select>

                    </div>
                </div>
                <div class="form-group">
                    <label>Minimal</label>
                    <select class="form-control select2 select2-hidden-accessible" style="width: 100%;" data-select2-id="1" tabindex="-1" aria-hidden="true">
                      <option selected="selected" data-select2-id="3">Alabama</option>
                      <option data-select2-id="30">Alaska</option>
                      <option data-select2-id="31">California</option>
                      <option data-select2-id="32">Delaware</option>
                      <option data-select2-id="33">Tennessee</option>
                      <option data-select2-id="34">Texas</option>
                      <option data-select2-id="35">Washington</option>
                    </select><span class="select2 select2-container select2-container--default select2-container--below" dir="ltr" data-select2-id="2" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-disabled="false" aria-labelledby="select2-b1zb-container"><span class="select2-selection__rendered" id="select2-b1zb-container" role="textbox" aria-readonly="true" title="Alabama">Alabama</span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span>
                  </div>
            </div>


            <div class="row">
                <div class="col-sm-3">
                    <!-- textarea -->
                    <label>Kode produk</label>
                    <div class="form-group">
                        <input type="text" id="kode_produk" class='form-control' name="kode_produk"
                            value=>
                    </div>
                </div>
            </div>

            <div class="col-sm-3">
                <!-- textarea -->
                <label>Tanggal Kejadian</label>
                <div class="form-group">
                    <input type="date" id="date" class='form-control' name="tgl_kejadian"
                        value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>
                </div>
            </div>

            <div class="col-sm-3">
                <!-- textarea -->
                <label>Tanggal Kejadians</label>
                <div class="form-group">
                    <input type="date" id="date" class='form-control' name="tgl_kejadian"
                        value='{{currLed.tanggal_kejadian| date:"Y-m-d"}}'>
                </div>
            </div>





            <div class="text-center">
                <button type="submit" class="btn btn-primary">Create</button>
            </div>

        </form>
    </div>
    <!-- /.card-body -->
</div>





{% endblock container-1 %}

{% block script-container-1 %}

{% endblock script-container-1 %}
