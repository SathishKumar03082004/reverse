<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <style>
        .sidebar {
            height: 100%;
            width: 200px;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #5592ce;
            padding-top: 20px;
        }

        .sidebar a {
            padding: 16px;
            text-decoration: none;
            font-size: 18px;
            color: white;
            display: block;
        }

        .sidebar a:hover {
            background-color: #ddd;
            color: rgb(255, 255, 255);
        }

        .main-container {
            margin-left: 190px;
            padding: 20px;
        }

        footer {
            background-color: #5592ce;
            color: #fff;
            padding: 10px;
            text-align: center;
            width: 100%;
            position: absolute;
            bottom: 0;
        }

        h1{
            color: rgb(54, 204, 209);
        }

        h3{
            color: burlywood;
        }
        h2{
            color: #33ff33;
        }
        .top-dashboard {
            background-color: #343a40;
            color: #fff;
            padding: 10px;
            text-align: center;
            position: relative; 
        }

        .top-dashboard h1 {
            margin-bottom: 1px;
            color: #fff;
        }
        .icon{
            position: absolute;
            margin-left: 45rem;
            margin-top: -2rem;
        }
        .notification{
            position: absolute;
            margin-left: 42rem;
            margin-top: -1.9rem;
            cursor: pointer;
        }
        .notification-popup {
            position: absolute;
            top: 30px;
            right: 0;
            background-color: #66ccff;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            display: none;
        }
    </style>
</head>

<body>

<div class="top-dashboard">
    <h1>Dashboard</h1>
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="icon bi bi-person-circle" viewBox="0 0 16 16" onclick="showLogoutPopup()">
        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
    </svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="notification bi bi-bell-fill" viewBox="0 0 16 16" onclick="showLogoutPopup()">
        <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2m.995-14.901a1 1 0 1 0-1.99 0A5 5 0 0 0 3 6c0 1.098-.5 6-2 7h14c-1.5-1-2-5.902-2-7 0-2.42-1.72-4.44-4.005-4.901"/>
    </svg>
    
    <div id="notificationPopup" class="notification-popup">
        <div class="popup-content">
            <h2>No notifications</h2>
            <button id="closePopupBtn">Close</button>
        </div>
    </div>
</div>

<div id="logout" class="notification-popup">
        <div class="popup-content">
            <h2>No notifications</h2>
            <button id="closePopupBtn">Close</button>
        </div>
    </div>
</div>

<div id="logoutPopup" class="popup-overlay" style="display: none;">
    <div class="popup-content">
        <h2>Logout Popup</h2>
        <p>Are you sure you want to logout?</p>
        <button class="close-btn" onclick="closePopup()">Close</button>
    </div>
</div>

<div class="sidebar">
    <center>
        <h2>Hotel</h2>
    </center>
    <a class="nav-link active" href="/dashboard">Dashboard</a>
    <a class="nav-link active" href="/update">Attendance Details</a>
</div>
<footer>
    <p>&copy; 2024 App. All rights reserved.</p>
    <p>Developed By <a href="https://sathish3.godaddysites.com">Sathish Kumar G</a></p>
</footer>

<script>
    function showLogoutPopup() {
        var popup = document.getElementById("notificationPopup");
        popup.style.display = "block";
    }

    function out{
        var popup = document.getElementById("logout");
        popup.style.display = "block";
    }

    function showLogoutPopup() {
        var popup = document.getElementById("logoutPopup");
        popup.style.display = "flex";
    }
</script>

</body>
</html>
