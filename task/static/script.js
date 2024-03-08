function confirmarEliminacion(taskId) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "Una vez eliminado, no podrás recuperar este registro",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, eliminarlo",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            // Si el usuario confirma, se envía el formulario para eliminar
            document.getElementById('delete-form-' + taskId).submit();
        } else {
            // Si el usuario cancela, no se hace nada
            Swal.fire("Operación cancelada", "", "info");
        }
    });
}


