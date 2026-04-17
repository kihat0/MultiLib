const popup = document.getElementById('active');
const button = document.getElementById('menu');

button.addEventListener('click', function() {
	popup.style.display = 'block';
        
});

window.addEventListener('click', function(event) {
	if (event.target === popup) {
	    popup.style.display = 'none';
	}     
});