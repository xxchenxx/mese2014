CKEDITOR.plugins.add('file', {
	init: function(editor){
		var config = editor.config.upload, fileId=config.fileId, queueId = config.queueId, $file=$("#"+fileId), $queue=$("#"+queueId), insertion="<a src='{url}' >{name}</a>",
		uploaderConfig=clone(config.uploader)||{};
		console.log(uploaderConfig);
		uploaderConfig.buttonText=uploaderConfig.buttonText||"选择上传文件";
		uploaderConfig.uploader = '/api/files/public/';
		uploaderConfig.fileObjName='file';
		uploaderConfig.swf='/static/img/uploadify.swf';
		uploaderConfig.auto=true;
		uploaderConfig.queueId=queueId;
		uploaderConfig.onUploadSuccess=function (file, data) {
				var data = decodeJSON(data);
				editor.insertHtml(window.uploadInsertion.replace('{url}', data.url).replace('{name}', data.name));
				uploaderConfig.callback&&uploaderConfig.callback(data);
		};
		uploaderConfig.onUploadComplete=function (){ $queue.hide();};
		console.log(uploaderConfig);
		$queue.hide();
		$file.uploadify(uploaderConfig);
		editor.addCommand( 'file',
		{
			exec : function( editor )
			{    
				window.uploadInsertion=insertion;
				$queue.show();
			}
		});
	editor.ui.addButton( 'file',
		{
			label: '文件',
			command: 'file',
			icon: this.path + 'icon.png'
		} );
	},
	onLoad:function(){}
});