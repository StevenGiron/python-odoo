function onchange_voting_process() {
    let votingIf = $('#voting_process_id').val();

    $.ajax({
        url: '/get_candidates/' + votingIf,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            let candidatesSelect = $('#candidate_id');
            candidatesSelect.empty();

            let candidates = data.candidates;

            console.log(candidates);

            $.each(candidates, function(index, candidate) {
                const optionElement = $('<option>');
                optionElement.val(candidate.id);
                optionElement.text(candidate.label);
                candidatesSelect.append(optionElement);
            });
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
}
