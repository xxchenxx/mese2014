$(document).ready(
  function(){
    $("#login-form").submit(function(e){
	e.preventDefault();
	validate_form();
    return false;
})});
function validate_form() {
  var uname=$("#inputUsername");
  var pword=$("#inputPassword");
  if(!(uname.val()&&pword.val())) {
	  add_error("empty");
  }
  else login();
}
function add_error(type) {
	if(type==="empty") {
	    $("#ufg").addClass("has-error");
	    $("#pfg").addClass("has-error");
		$("#Result").text("用户名或密码不能为空").addClass("visible");
	}
	else if(type==="error"){
      $("#ufg").addClass("has-error");
	    $("#pfg").addClass("has-error");
		 $("#Result").text("用户名或密码错误").addClass("visible");
	}
}
function clean_form() {
	var uname=$("#inputUsername");
    var pword=$("#inputPassword");
	$("#ufg").removeClass("has-error");
	$("#pfg").removeClass("has-error");
	if($("#Result").hasClass("visible")){
	    uname.val("");
	    pword.val("");
	}
	$("#Result").val("").removeClass("visible");
}
function login() {
	$.ajax({
		async:true,
		url : "/accounts/login/",
		data : $('#login-form').serialize(),
		type:"POST",
		dataType:"json",
		success: function(data) {
			window.location.href = data.referer;
		},
		statusCode: {
			400: function (data) {
				add_error("error");
			}
		}
	});
}