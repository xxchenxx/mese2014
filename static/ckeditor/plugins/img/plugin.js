CKEDITOR.plugins.add('img', {
	init: function(editor){
		var config = editor.config.upload, fileId=config.fileId, formId=config.formId, queueId = config.queueId, $file=$("#"+fileId), $queue=$("#"+queueId), $form=$("#"+formId), insertion="<img src='{url}' />", callback = config.callback||function(){};
		$form.hide();
		$form.fileupload({
			url: "/api/files/public/",
			autoUpload: true,
			dataType: 'json',
			formAcceptCharset: "unicode",
			done: function (e, xhr) {
				var data = xhr.result;
				editor.insertHtml(window.uploadInsertion.replace('{url}', data.url).replace('{name}', data.name));
				callback(data);
				$form.hide();
			}
		});
		editor.addCommand( 'img',
		{
			exec : function( editor )
			{    
				window.uploadInsertion=insertion;
				$form.show();
			}
		});
	editor.ui.addButton( 'img',
		{
			label: '图片',
			command: 'img',
			icon: this.path + 'icon.png'
		} );
	},
	onLoad:function(){}
});
