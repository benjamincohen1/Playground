var each=function(l,fun){
	for (var i =0;i<l.length;i++){
		fun(l[i])
	}
};

var map=function(l,fun){
	var r=new Array();
	for (var i =0;i<l.length;i++){
		r[i]=(fun(l[i]))

	}
	return r
};

var find=function(l,fun){
	var r=new Array();
	for (var i =0;i<l.length;i++){
		if(fun(l[i])){
			r.push(l[i]);
		}
	}
	return r;
};

var reject=function(l,fun){
	var r=new Array();
	for (var i =0;i<l.length;i++){
		if(!fun(l[i])){
			r.push(l[i]);
		}
	}
	return r;
};

var every=function(l,fun){
	for (var i =0;i<l.length;i++){
		if(!fun(l[i])){
			return false;
		}
	}
	return true;
};

var some=function(l,fun){
	for (var i =0;i<l.length;i++){
		if(fun(l[i])){
			return false;
		}
	}
	return true;
};

var contains=function(l,value){
	for (var i =0;i<l.length;i++){
		if(l[i]==value){
			return true;
		}
	}
	return false;
};
var invoke=function(l,func){
	var r=new Array();
	for (var i =0;i<l.length;i++){
		r.push(func(l[i]));
	}
	return r;
};

var max=function(l,func){
	var r=l[0];
	for (var i =1;i<l.length;i++){
		if(func(l[i])>func(r)){
			r=l[i]
		}
	}
	return r;
};
var min=function(l,func){
	var r=l[0];
	for (var i =1;i<l.length;i++){
		if(func(l[i])<func(r)){
			r=l[i]
		}
	}
	return r;
};
var first=function(array,n){
	if(n==undefined){
		n=0;
	}
	var r=new Array();
	for(var i =0;i<n;i++){
		r.push(array[i]);
	}
	return r;
}
var intiial=function(array,n){
	if(n==undefined){
		n=0;
	}
	var r=new Array();
	for(var i =0;i<array.length-n;i++){
		r.push(array[i]);
	}
	return r;
}
