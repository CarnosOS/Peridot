WeatherTarp.controller('MainController', ['$scope', 'weather',
function($scope, weather) {
weather.success(function(data){
 
$scope.fiveDay = data;
  });
}]);