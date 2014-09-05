
UserModel = Backbone.Model.extend({
  
	initialize: function() {
	},
	
	urlRoot : function(){
    	return '/api/v1/user/';
	},
	
});


var Users = Backbone.Collection.extend({

	model: UserModel,
	
	url : '/api/v1/user/',
	
});

users = new Users;