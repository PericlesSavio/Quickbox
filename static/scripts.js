// Template data
const dataEl = document.getElementById('templateData');
const texts = JSON.parse(dataEl.dataset.texts);
const currentPath = JSON.parse(dataEl.dataset.currentPath);
const enableDragDrop = JSON.parse(dataEl.dataset.enableDragDrop);


// Global variables for upload
let fileQueue = [];
let modalActive = false;


// File upload function
function sendFile(file) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('current_path', currentPath);

    fetch('/upload', { method: 'POST', body: formData })
        .then(res => {
            if(res.ok) {
                fileQueue.shift(); // remove the file from the queue
                if(fileQueue.length > 0) processNextFile();
                else window.location.reload();
            } else alert('Erro ao enviar o arquivo');
        })
        .catch(err => alert('Erro ao enviar o arquivo: ' + err));
}


// Overwrite modal
function handleOverwrite(yes) {
    document.getElementById('overwriteModal').style.display = 'none';
    modalActive = false;
    const file = fileQueue[0];
    if(yes && file) sendFile(file);
    else {
        fileQueue.shift(); // remove the file from the queue
        processNextFile();
    }
}


// Process next file in the queue
async function processNextFile() {
    if(fileQueue.length === 0 || modalActive) return;
    const file = fileQueue[0];

    const formDataCheck = new FormData();
    formDataCheck.append('filename', file.name);
    formDataCheck.append('current_path', currentPath);

    const response = await fetch('/check_file', { method: 'POST', body: formDataCheck });
    const result = await response.json();

    if(result.exists) {
        modalActive = true;
        document.getElementById('overwriteMessage').textContent =
            texts.overwrite_message.replace('{filename}', file.name);
        document.getElementById('overwriteModal').style.display = 'flex';
    } else {
        sendFile(file);
    }
}


// Drag & Drop - entire page
if(enableDragDrop) {
    const dragOverlayMessage = document.getElementById('dragOverlayMessage');
    let dragCounter = 0;

    // Show overlay on dragenter anywhere on the page
    document.addEventListener('dragenter', e => {
        e.preventDefault();
        dragCounter++;
        dragOverlayMessage.style.display = 'flex';
    });

    // Prevent default dragover
    document.addEventListener('dragover', e => e.preventDefault());

    // Hide overlay when leaving the page
    document.addEventListener('dragleave', e => {
        e.preventDefault();
        dragCounter--;
        if(dragCounter === 0) dragOverlayMessage.style.display = 'none';
    });

    // Handle dropped files anywhere on the page
    document.addEventListener('drop', e => {
        e.preventDefault();
        dragCounter = 0;
        dragOverlayMessage.style.display = 'none';
        const files = Array.from(e.dataTransfer.files);
        fileQueue.push(...files);
        if(!modalActive) processNextFile();
    });
}


// Upload button
const uploadBtn = document.getElementById('uploadBtn');
const fileInput = document.getElementById('fileInput');

uploadBtn.addEventListener('click', () => {
    const files = Array.from(fileInput.files);
    if(files.length === 0) return;

    files.forEach(f => f.name = encodeURIComponent(f.name));
    fileQueue.push(...files);
    if(!modalActive) processNextFile();
});
