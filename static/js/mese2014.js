$(document).ready(function(){
	$.ajaxSetup({
	  dataType:"json"	
	})
})
function sendfeeds(){
	var p = $("#p_new").serializeObject();
	p['content'] = CKEDITOR.instances['text'].getData();
	console.log(p);
	$.ajax({
		url:"/api/passages/",
		type:"POST",
		data:p,
	})
}
function MESEIO(){}
(function(){
		MESEIO.prototype.loadfeeds = function(type){
			if(!type) {utype="";}
			else (utype="?type="+type)
			var api_url = '/api/passages/'+utype;
			$.ajax({
				url:api_url,
				type:"GET",
				success:function(data){
					$.each(data.results,function(){
						var pt=this.title, pk='';
						if((this.type=="GOV")||(this.type=="CON")){
							pk = "<i class='fa fa-bank' />";
						}
						else if (this.type=="MED"){
							pk = "<i class='fa fa-rss' />";
						}
						var pi = "<em class='pull-right feeds-info'>"+this.author.profile.display_name  
						+"@"+this.year + "</em>";
						$("#feeds-container").append("<div class='feeds'><div class='feeds-title'>"+pk 
						+ "<a href='?id=" + this.id + "'>" + pt + "</a>" + pi);
					})
				}
			})
		}
		MESEIO.prototype.loadfdetails = function(id){
			var api_url = "/api/passages/"+id;
			$.ajax({
				url:api_url,
				type:"GET",
				success:function(data){
					var f_back = "<li class='active'>新闻正文</li>"
					$('.breadcrumb-mese2014').children('.active').removeClass('active').html("<a href='?type="+data.type+"'>信息中心</a>");
					$('.breadcrumb-mese2014').append(f_back);
					var text=("<h3 class='text-center feeds-details-title'>{title}</h3><div class='text-center feeds-details-info'>{created_time} by @{author.profile.display_name}</div><div class='feeds-details-text'>{content}</div>").render(data);
					$("#feeds-container").append(text);	
				},
			})			
		}
})();
(function($){
$.getUrlParam = function(name){
var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
var r = window.location.search.substr(1).match(reg);
if (r!=null) return unescape(r[2]);return null;
}
})(jQuery);
