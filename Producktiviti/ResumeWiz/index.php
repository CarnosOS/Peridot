<!DOCTYPE HTML>
<html>
<head>
<title>Resume Wiz</title>
<script src="/core/js/angularjs/angular.min.js"></script>
<script>
var rmwz = angular.module("ResumeWiz",[]);
rmwz.controller("HomeController",["$scope", function($scope){
   $scope.ResumeWiz = { 
     title: "ResumeWiz 1", 
     name: "My Resume",
     tuition: 20000,
     today: new Date(),
     resumes: [{
     name: "My Resume",
     date: new Date(),
     portrait: '/core/media/img/notidar.png'
},
{
name: "Your Resume",
date:  new Date()
}]};

}]);
</script>
</head>
<body ng-app="ResumeWiz">
<div class="main" ng-controller="HomeController">
<h1 classs="title">{{ ResumeWiz.title | uppercase }}</h1>
<p class="money">{{ ResumeWiz.tuition | currency }}</p>
<p class="date">{{ ResumeWiz.today | date }}</p>
<div ng-repeat="resume in ResumeWiz.resumes">
  <p class="title-resume">{{ resume.name }}</p>
  <p class="date-resume">{{ resume.date | date }}</p>
  <img ng-src="{{ resume.portrait }}">
</div>
</div>
</body>
</html>