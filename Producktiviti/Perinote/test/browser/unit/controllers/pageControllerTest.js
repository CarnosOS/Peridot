define(function () {

    'use strict';

    describe('PageController', function() {

        beforeEach(module('perinote'));

        it('foo returns proper value', inject(function($rootScope, $controller) {

            var $scope = $rootScope.$new();
            var controller = $controller('PageController', { $scope : $scope });

            expect($scope.foo).to.equal('World!');
        }));
    });
});