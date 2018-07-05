;
! function() {
	var layer = layui.layer,
		form = layui.form;


	// 自定义验证规则
	form.verify({
		regexit: function() {
			vailPhone();
			if(phone_status == 0) {
				return "该手机号已被注册";
			}
		},
		pwd: function(value) {
			if(value.length < 8) {
				return "密码长度不能少于8位";
			} else if(!/^(\w){8,20}$/.test(value)) {
				return "密码只能包含字母、数字或下划线";
			}
		},
		rePwd: function(value) {
			if(value != $("#password").val()) {
				return "两次输入的密码不一致";
			}
		},
	});

	//监听提交  
	form.on("submit(register)", function() {
		if(phone_status == 0) {
			layer.msg("该手机号已被注册", {
				icon: 5
			});
		} else if(msg_send_count == 0) {
			layer.msg("请点击获取验证码");
		} else {
			$.ajax({
				url: "user/vailSMSCode.do",
				type: "post",
				async: false,
				data: {
					"code": $("#msg-code").val()
				},
				success: function(result) {
					if(result.status == 1) {
						layer.msg(result.msg);
						return false;
					} else {
						// 发送注册请求到后台匹配
						$.ajax({
							url: "user/register.do",
							type: "post",
							data: {
								"tel": $("#phone").val(),
								"password": $("#password").val(),
								"username":$("#username").val(),
								"email":$("#email").val()
							},
							success: function(result) {
								if(result.status == 0) {
									layer.msg("注册成功");
									setTimeout("location='login.html'", 2000);
								} else {
									$("form")[0].reset();
									layer.msg(result.msg, {
										icon: 5
									});
								}
							}
						});
					}
				}
			});
		}

		return false;
	});
}();