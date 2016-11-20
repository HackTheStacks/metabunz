app.directive('keywordSearch', function ($state) {
    return {
        restrict: 'E',
        templateUrl: 'js/search/search.html',
        controller: 'searchCrl'
    };
});
app.service('searchService', function(){
	var searchword = "";
	var addsearchword = function(_searchword){
		searchword = _searchword;
	}
	var getsearchword = function(){
		if(searchword.length>=1) return searchword;
		else return "";
	}
	return {
		addsearchword: addsearchword,
		getsearchword: getsearchword
	};
});
app.controller('searchCrl', function($scope,$window,$state,searchService){

	var recognition = new $window.webkitSpeechRecognition();
	recognition.continuous = true;
	//recognition.interimResults = true;
	
	var text = $window.document.getElementById('textinput');
	recognition.onend = function(event){
		if(event) $scope.reset();
	};
    
	$scope.submit = function(event){
		console.log("text", text.value);
		$scope.keyword = text.value;
        searchService.addsearchword($scope.keyword);
        console.log("searchword", searchService.getsearchword());
		console.log("evetKeycode",event.keyCode);

		if(event.keyCode === 13) {
			recognition.stop();
			console.log("In side of if");
			$state.go("results",{searchword:text.value});
		}
	}
	recognition.onresult = function (event) {
          for (var i = event.resultIndex; i < event.results.length; ++i) {
            // if (!event.results.final) {
            // 	text.value += event.results[i][0].transcript;
            //     console.log("text value:", text.value);
            // }
            if (!event.results.final) {
            	text.value = event.results[i][0].transcript;
                console.log("text value:", text.value);
            }

          }
        $scope.keyword = text.value;
        searchService.addsearchword($scope.keyword);
         // $scope.keyword = event.results[0][0].transcript;
        // $scope.confidence =  event.results[0][0].confidence;
    };
    $scope.reset = function () {
        $scope.isSpeaking = false; 
    }
	$scope.isSpeaking = false;
	$scope.toggleStartStop = function(){
		if($scope.isSpeaking){
			recognition.stop();
			$scope.isSpeaking = !$scope.isSpeaking;
			console.log("when stop keyword", $scope.keyword);

		}
		else {
			$scope.reset();
			$scope.keyword = 0;
         	text.value = "";
			$scope.isSpeaking = !$scope.isSpeaking;
			recognition.start();
			console.log("when start keyword", $scope.keyword);
		}
	}	
})