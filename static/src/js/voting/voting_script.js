function updateCandidates() {
    let process_id = $('#process_id').value
    console.log(process_id)
    $.ajax({
        url: '/get_candidates',
        type: 'POST',
        data: {
            'voting_process_id': process_id,
        },
        dataType: 'json',
        success: function(data) {
            var candidateSelect = $('select[name="candidate"]');
            candidateSelect.empty(); // Limpiar opciones actuales
            $.each(data, function(index, candidate) {
                candidateSelect.append($('<option>', {
                    value: candidate.id,
                    text: candidate.name
                }));
            });
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });

