<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
    <title>Fruit Store</title>



</head>
<body class="container">
<h1 id="head">Fruit Store</h1>
<c:forEach var="fruit" items="${fruits}">
    <div class="fruit">
        <table class="table table-hover even-row-color">
            <thead>
            <tr>
                <th>Name</th>
                <th>Price</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>${fruit.name}</td>
                <td>$${fruit.price}</td>
            </tr>
            </tbody>
        </table>
    </div>
</c:forEach>
</body>
</html>
