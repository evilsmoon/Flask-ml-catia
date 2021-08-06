function predicttext() {
    if (!$("#inputText").val()) {
        alert("Ingresa su definicion de demencia");
        return;
      }
      $.ajax({
        url: "/predic",
        type: "POST",
        data: JSON.stringify({ answer: $("#inputText").val() }),
        success: function (data) {
          resp = JSON.parse(data);
          console.log(resp);
          if (resp) {
            $("#similitudJC").attr("hidden", false).html(`
                <div class='container'>
                <h3 class="margin text-danger">Cálculo de Similitudes y Tipo de Enfoque</h3>
                <table class="table">
                <thead>
                  <th></th>
                  <td>ENFOQUE PSICOSOCIAL - COMUNITARIO</td>
                  <td>MODELO BIO MEDICO</td>
                  <td>ENFOQUE COTIDIANO</td>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">Similitud Jaccard</th>
                    <td>${resp.jacc_epc.toFixed(4)}</td>
                    <td>${resp.jacc_mbm.toFixed(4)}</td>
                    <td>${resp.jacc_ec.toFixed(4)}</td>
                  </tr>
                  <tr>
                    <th scope="row">Similitud Coseno</th>
                    <td>${resp.cos_epc.toFixed(4)}</td>
                    <td>${resp.cos_mbm.toFixed(4)}</td>
                    <td>${resp.cos_ec.toFixed(4)}</td>
                  </tr>
                </tbody>
              </table>
                </div>
            `);
          }
          setTimeout(() => {
          }, 500);
        },
        error: function (err) {
          setTimeout(() => {
          }, 500);
          console.log(err);
        },
      });
}
//   resp = JSON.parse(data);
// console.log(resp);
