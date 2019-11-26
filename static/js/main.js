function send() {
	if (document.getElementById('file').files.length > 0) {
		// Get file from file input
		var file = document.getElementById('file').files[0];

		// Get code number
		var code = document.getElementById('code').value;

		// Create FormData
		var formData = new FormData();
		formData.append("image", file);
		
		// Request to the server
		var xhr = new XMLHttpRequest();
		xhr.open('POST', `img2text?code=${code}`, true);
		xhr.send(formData);

		// Set response to #text
		xhr.onload = () => {
			document.getElementById("text").value = xhr.responseText;
		};


		// Show opened file in #viewerImg
		var reader = new FileReader();
		var imgtag = document.getElementById("viewerImg");
		imgtag.title = file.name;
		reader.onload = function(event) {
			imgtag.src = event.target.result;
			
			// Download button
			document.getElementById('download').href = event.target.result;
			document.getElementById('download').download = 'image.png';
			document.getElementById('download').style.visibility = "visible";
		};
		
		reader.readAsDataURL(file);
	} else if (document.getElementById('text').value) {
		// Get message from text input
		var text = document.getElementById('text').value;

		// Filter string from new line
		var data = encodeURIComponent(text);

		// Get code number
		var code = document.getElementById('code').value;

		// Set response image to #viewerImg
		document.getElementById("viewerImg").src = `text2img?data=${data}&code=${code}`;

		// Download button
		document.getElementById('download').href = `text2img?data=${data}&code=${code}`;
		document.getElementById('download').download = 'image.png';
		document.getElementById('download').style.visibility = "visible";

	}
}