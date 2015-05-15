requirejs.config({

    baseUrl: '/',

    paths: {

        'jquery': 'components/jquery/jquery',

        'angular': 'components/angular/angular',
        'angularRoute': 'components/angular-route/angular-route',

        'pageController': 'js/controllers/pageController',

        'app': 'js/app',
        'config': 'js/config',
        'routes': 'js/routes'
    },

    shim: {

        'jquery': {
            exports: 'jQuery'
        },
        'angular': {
            deps: [ 'jquery' ],
            exports: 'angular'
        },
        'angularRoute': {
            deps: [ 'angular' ]
        }
    }
});


require([

    'angular',
    'config',
    'routes'

], function(angular) {

    'use strict';

    angular.bootstrap(document, ['perinote']);
});
