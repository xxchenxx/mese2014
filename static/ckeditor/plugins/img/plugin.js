CKEDITOR.plugins.add('img', {
	init: function(editor){
		var config = editor.config;
		var fileId=config.fileId, queueId = config.queueId, insertion="{url}";
		console.log(fileId+queueId);
		$('#'+fileId).uploadify({
			uploader: '/api/files/',
			fileObjName: 'file',
			swf: '/static/img/uploadify.swf',
			auto: true,
			queueID: queueId,
			onUploadSuccess: function (file, data) {
				var data = eval('('+data+')');
				editor.insertHtml(insertion.replace('{url}', data.url).replace('{name}', data.name));
			}
		});
		editor.addCommand( 'img',
	{
		exec : function( editor )
		{    
			var fileId = editor.config.fileId;
			$('#'+fileId).click().uploadify('upload');
		}
	});
	editor.ui.addButton( 'img',
		{
			label: 'Insert Timestamp',
			command: 'img',
			icon: this.path + 'noimage.png'
		} );
	},
	onLoad:function(){}
});

/*(function(){
	var _plugin = function (insertion) {
		this.exec = function(editor) {
			var fileId = editor.config.fileId;
			$('#'+fileId).uploadify('upload');
		};
	};
	var cmds = [
		{name: 'img',
		lb: 'Í¼Æ¬',
		plugin: new _plugin('<img src="{url}"></img>'),
		icon: "/static/ckeditor/plugins/upload/noimage.png"},
		{name: 'file',
		lb: 'ÎÄ¼þ',
		plugin: new _plugin('<a href="{url}">{name}</a>'),
		icon: "/static/ckeditor/plugins/upload/noimage.png"}
	];
	for (var i=0;i<cmds.length;i++) {
		var cmd = cmds[i];
		console.log(cmd);
		CKEDITOR.plugins.add(cmd.name, {
			init: function(editor){
				var config = editor.config;
				var fileId=config.fileId, queueId = config.queueId;
				$('#'+fileId).uploadify({
					uploader: '/api/files/',
					fileObjName: 'file',
					auto: true,
					queueId: queueId,
					onUploadSuccess: function (file, data) {
						var data = eval('('+data+')');
						editor.insertHtml(insertion.replace('{url}', data.url).replace('{name}', data.name));
					}
				});
				editor.addCommand(cmd.name, cmd.plugin);
				editor.ui.addButton(cmd.name, {
					label: cmd.lb,
					icon: cmd.icon,
					command: cmd.plugin
				});
			}
		});
	}
});*/