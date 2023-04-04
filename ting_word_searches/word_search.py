def exists_word(word, instance):
    """Aqui irá sua implementação"""
    allData = instance.seeData()
    result = []
    for data in allData:
        res = {
            "palavra": word,
            "arquivo": data['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index, line in enumerate(data['linhas_do_arquivo']):
            if word.lower() in line.lower():
                res['ocorrencias'].append({
                    'linha': index + 1
                })
        if len(res['ocorrencias']) > 0:
            result.append(res)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    allData = instance.seeData()
    result = []
    for data in allData:
        res = {
            "palavra": word,
            "arquivo": data['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index, line in enumerate(data['linhas_do_arquivo']):
            if word.lower() in line.lower():
                res['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': line
                })
        if len(res['ocorrencias']) > 0:
            result.append(res)
    return result
