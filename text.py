def situation_singular(scene_situation, interdition_situation):

    if interdition_situation:
        return (
            'No momento da chegada da equipe, o local estava sinalizado pela'
            ' viatura da Concessionária da Rodovia. '
            'O veículo se encontrava no acostamento da via, conforme '
            'fotografias adicionadas neste LPAT. '
            f'Houve interdição {interdition_situation} da via - comprometendo'
            'a fluidez do trânsito. '
            'A dinâmica do acidente encontra-se representada no croqui -'
            f'A cena encontrava-se {scene_situation} quando da chegada'
            'da equipe.'
        )

    else:
        return (
            'No momento da chegada da equipe, o local estava sinalizado pela '
            'viatura da Concessionária da Rodovia. '
            'O veículo se encontrava no acostamento da via, conforme '
            'fotografias adicionadas neste LPAT. '
            'Não houve interdição da via - permanecendo o trânsito fluindo em '
            'todas as faixa. A dinâmica do acidente encontra-se representada '
            f'no croqui. A cena encontrava-se {scene_situation} '
            'quando da chegada da equipe.'
        )


def situation_plural(scene_situation, interdition_situation):
    if interdition_situation is not None:
        return (
            'No momento da chegada da equipe, o local estava sinalizado pela '
            'viatura da Concessionária da Rodovia. '
            'Os veículos se encontravam no acostamento da via, conforme '
            'fotografias adicionadas neste LPAT. '
            f'Houve interdição {interdition_situation} da via - comprometendo '
            'a fluidez do trânsito. A dinâmica do acidente encontra-se '
            f'representada no croqui - A cena encontrava-se {scene_situation} '
            'quando da chegada da equipe.'
        )
    else:
        return (
            'No momento da chegada da equipe, o local estava sinalizado '
            'pela viatura da Concessionária da Rodovia. '
            'O veículo se encontrava no acostamento da via, '
            'conforme fotografias adicionadas neste LPAT. '
            'Não houve interdição da via - permanecendo o trânsito fluindo '
            'em todas as faixa. '
            'A dinâmica do acidente encontra-se representada no croqui '
            f'- A cena encontrava-se {scene_situation} quando da '
            'chegada da equipe.'
        )
