import streamlit as st
import streamlit.components.v1 as stc

stc.html(
    """
    <script src="https://rawgit.com/sitepoint-editors/jsqrcode/master/src/qr_packed.js"></script>
	<input type=text size=16 placeholder="Tracking Code" class=qrcode-text><label class=qrcode-text-btn><input type=file accept="image/*" capture=environment onclick="return showQRIntro();" onchange="openQRCamera(this);" tabindex=-1></label> 
	<input type=button value="Go" disabled>
	<style>
		input {font-size:14pt}
		input, label {vertical-align:middle}
		.qrcode-text {padding-right:1.7em; margin-right:0}
		.qrcode-text-btn {display:inline-block; background:url(//dab1nmslvvntp.cloudfront.net/wp-content/uploads/2017/07/1499401426qr_icon.svg) 50% 50% no-repeat; height:1em; width:1.7em; margin-left:-1.7em; cursor:pointer}
		.qrcode-text-btn > input[type=file] {position:absolute; overflow:hidden; width:1px; height:1px; opacity:0}
	</style>
	<script>
		function openQRCamera(node) {
			var reader = new FileReader();
			reader.onload = function() {
				node.value = "";
				qrcode.callback = function(res) {
				if(res instanceof Error) {
					alert("No QR code found. Please make sure the QR code is within the camera's frame and try again.");
				} else {
					node.parentNode.previousElementSibling.value = res;
				}
			};
			qrcode.decode(reader.result);
		};
		reader.readAsDataURL(node.files[0]);
		}

		function showQRIntro() {
		return confirm("カメラを使用してQRコードの写真を撮ります。");
		}
	</script>
	"""
)
