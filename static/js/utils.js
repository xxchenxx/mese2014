function clone(obj){ 
	if(typeof(obj) !== 'object'||obj===null) return obj;  
	var newobj = new Object(); 
	for(var i in obj) newobj[i] = clone(obj[i]); 
	return newobj; 
}
function JsonToStr(o) {
	if (o === undefined) {
		return "";
	}
	var r = [];
	if (typeof o === "string") return "\"" + o.replace(/([\"\\])/g, "\\$1").replace(/(\n)/g, "\\n").replace(/(\r)/g, "\\r").replace(/(\t)/g, "\\t") + "\"";
	if (typeof o === "object") {
		if (!o.sort) {
			for (var i in o)
				r.push("\"" + i + "\":" + JsonToStr(o[i]));
			if (!!document.all && !/^\n?function\s*toString\(\)\s*\{\n?\s*\[native code\]\n?\s*\}\n?\s*$/.test(o.toString)) {
				r.push("toString:" + o.toString.toString());
			}
			r = "{" + r.join() + "}"
		} else {
			for (var i = 0; i < o.length; i++)
				r.push(JsonToStr(o[i]))
			r = "[" + r.join() + "]";
		}
		return r;
	}
	return o.toString().replace(/\"\:/g, '":""');
}
window.encodeJSON = JSON.stringify||JsonToStr;
window.decodeJSON = JSON.parse||function(d){eval('('+d+')')};

String.prototype.render = function(context) {
	return this.replace(/{([^{}]+)}/g, function (word) {
		var words=word.slice(1,-1).split(),obj=context;
		for (var i=0,l=words.length;i<l;i++){
			obj=context[words[i]];
			if (obj===undefined) return '';
		}
		return obj
	});
};

$.fn.serializeObject = function() {
	var o={}, a=this.serializeArray();
	console.log(a);
	$.each(a, function(){
		var value=this.hasOwnProperty('value')?this.value:'';
		if (typeof o[this.name]==="Array") {
			o[this.name].append(value)
		} else 
			(o[this.name]===undefined)?o[this.name]=value:o[this.name]=[o[this.name],value];
	});
	return o;
};

(function(){
	function ajax(url, data， method) {
		return $.ajax();
	}
	function API(data){
	
	}
})();
