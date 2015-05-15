<!doctype html>

<html lang="en">

<head>
  
<meta charset="UTF-8">
 
 <title>Example - Exprat</title>
  

  
<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.4.0-rc.1/angular.min.js"></script>

  <script src="script.js"></script>
  

  
</head>

<body ng-app="Exprat">
  
<div ng-controller="ExpratController" class="expressions">
  
Expression:
  <input type='text' ng-model="expr" size="80"/>
  
<button ng-click="addExp(expr)">Evaluate</button>
  
<ul>
   
<li ng-repeat="expr in exprs track by $index">
    
 [ <a href="" ng-click="removeExp($index)">X</a> ]
   
  <tt>{{expr}}</tt> => <span ng-bind="$parent.$eval(expr)"></span>
   
 </li>
  </ul>
</div>
</body>
</html>