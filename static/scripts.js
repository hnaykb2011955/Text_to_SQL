/* filepath: d:\project\Python\Text_To_SQL-main\templates\scripts.js */
// Tải danh sách database khi trang tải
window.onload = function() {
    fetch('/databases')
        .then(response => response.json())
        .then(data => {
            const databaseSelect = document.getElementById('database');
            data.databases.forEach(db => {
                const option = document.createElement('option');
                option.value = db;
                option.text = db;
                databaseSelect.add(option);
            });
        });
};

// Khi chọn database, tải danh sách bảng tương ứng
function fetchTables() {
    const database = document.getElementById('database').value;
    fetch(`/tables?database=${database}`)
        .then(response => response.json())
        .then(data => {
            const tableSelect = document.getElementById('table');
            tableSelect.innerHTML = ''; // Xóa danh sách cũ
            data.tables.forEach(table => {
                const option = document.createElement('option');
                option.value = table;
                option.text = table;
                tableSelect.add(option);
            });
        });
}