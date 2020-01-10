function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var year = document.getElementById("uiYear");
    var mileage = document.getElementById("uiMileage");
    var power = document.getElementById("uiPower");
    var brand = document.getElementById("uiBrand");
    var model_ = document.getElementById("uiModel");
    var body = document.getElementById("uiBody");
    var fuel = document.getElementsById("uiFuel");
    var transmission = document.getElementsById("uiTransmission");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_price";
  
    $.post(url, {
        year: parseFloat(year.value),
        mileage: parseFloat(mileage.value),
        power: parseFloat(power.value),
        brand: brand.value,
        model_: model_.value,
        body: body.value,
        fuel: fuel.value,
        transmission: transmission.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_brand_names";
    $.get(url,function(data, status) {
        console.log("got response for get_brand_names request");
        if(data) {
            var brand = data.brand;
            var uiLocations = document.getElementById("uiBrand");
            $('#uiBrand').empty();
            for(var i in brand) {
                var opt = new Option(brand[i]);
                $('#uiBrand').append(opt);
            }
        }
    });
  }

  function onPageLoadModel() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_model_names";
    $.get(url,function(data, status) {
        console.log("got response for get_model_names request");
        if(data) {
            var model = data.model;
            var uiLocations = document.getElementById("uiModel");
            $('#uiModel').empty();
            for(var i in model) {
                var opt = new Option(model[i]);
                $('#uiModel').append(opt);
            }
        }
    });
  }

  function onPageLoadBody() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_body_names";
    $.get(url,function(data, status) {
        console.log("got response for get_body_names request");
        if(data) {
            var body = data.body;
            var uiLocations = document.getElementById("uiBody");
            $('#uiBody').empty();
            for(var i in body) {
                var opt = new Option(body[i]);
                $('#uiBody').append(opt);
            }
        }
    });
  }

  function onPageLoadFuel() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_fuel_names";
    $.get(url,function(data, status) {
        console.log("got response for get_fuel_names request");
        if(data) {
            var fuel = data.fuel;
            var uiLocations = document.getElementById("uiFuel");
            $('#uiFuel').empty();
            for(var i in fuel) {
                var opt = new Option(fuel[i]);
                $('#uiFuel').append(opt);
            }
        }
    });
  }

  function onPageLoadTransmission() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_transmission_names";
    $.get(url,function(data, status) {
        console.log("got response for get_transmission_names request");
        if(data) {
            var transmission = data.transmission;
            var uiLocations = document.getElementById("uiTransmission");
            $('#uiTransmission').empty();
            for(var i in transmission) {
                var opt = new Option(transmission[i]);
                $('#uiTransmission').append(opt);
            }
        }
    });
  }
  
window.onload = onPageLoad();
window.onload = onPageLoadModel();
window.onload = onPageLoadBody();
window.onload = onPageLoadFuel();
window.onload = onPageLoadTransmission();


 