<!doctype html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="http://s3.amazonaws.com/codecademy-content/projects/bootstrap.min.css" rel="stylesheet" />
    <link href="css/main.css" rel="stylesheet" />
    
    <!-- Include the AngularJS library -->
    <script src="/core/js/angularjs/angular.min.js"></script>
  </head>
  <body ng-app="WeatherTarp">

    <div class="main" ng-controller="MainController">
      <div class="container">
        <div class="row">
          <div class="col-sm-5 col-sm-offset-7">
            <h1>{{ fiveDay.city_name }}</h1>
            <h2>5-day forecast</h2>
            <div class="forecast" ng-repeat="day in fiveDay.days">
              <div class="day row">

                <!-- datetime -->
                <div class="weekday col-xs-4">

                </div>


                <!-- icon -->
                <div class="weather col-xs-3">

                </div>

                <div class="col-xs-1"></div>


                <!-- high -->
                <div class="high col-xs-2">


                </div>


                <!-- low -->
                <div class="low col-xs-2">

                </div>
              </div>
            </div>
          </div>
        </div>
        </ul>
      </div>
    </div>

    <!-- Modules -->
    <script src="js/app.js"></script>

    <!-- Controllers -->
    <script src="js/controllers/MainController.js"></script>

    <!-- Services -->
    <script src="js/services/weather.js"></script>

    <!-- Directives -->

  </body>
</html>