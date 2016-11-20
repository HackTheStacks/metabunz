app.config(function ($stateProvider) {
    $stateProvider.state('results', {
        url: '/results',
        templateUrl: 'js/results/results.html',
        controller: 'resultsCtrl',
        resolve: { 
        	allResults: function(getresultsFactory){
        		return getresultsFactory.getResults();
        	}
    	}
    });
});

app.controller('resultsCtrl', function($scope, allResults, searchService, $stateParams) {
    $scope.searchword = searchService.getsearchword;
    $scope.results = allResults;
    console.log("results", $scope.results);    
 //    $scope.user = $stateParams.userId
});

app.factory('getresultsFactory', function($http){
    return {
        allResults: {
         "keyword": "Akeley-Eastman-Pomeroy African Hall Expedition of the American Museum of Natural History",
         "description": "The Akeley-Eastman-Pomeroy African Hall Expedition was a collecting expedition to Africa; its mission was to provide specimens for the African Hall at the American Museum of Natural History, originally conceived in 1910. The man behind both the exhibit hall and the expedition was Carl Ethan Akeley, an animal sculptor and taxidermist, an inventor, naturalist and photographer. The Eastman-Pomeroy expedition focused on collecting specimens for the dioramas of the African Hall, as well as accessories such as grass and bushes, and the creation of background paintings from artists William Leigh and Arthur August Jansson...",
         "doc_type": "expedition"
        },
        getResults: function(){

            return allResults;
            // return $http.get('/api/recipes')
            // .then(function(res){
            //     var results = angular.copy(res.data);
            //     if (results.length >= 30) return recipes.slice(0,30)
            //     else return recipes;
            // })

        }
    }
})