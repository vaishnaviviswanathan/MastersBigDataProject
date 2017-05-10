var bigDataApp = angular.module('bigDataApp', []);

bigDataApp.controller('bigDataAppController', function bigDataAppController($scope) {
	$scope.parts = [
		{
			name: 'title',
			snippet: 'this is the main setup for our angular js app'
		},
		{
			name: 'body',
			snippet: 'this is just to test things'
		}
	];
});
