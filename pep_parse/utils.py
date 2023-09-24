def make_rows(
        status_count: dict[str: int],
        total: int
) -> list[dict[str: int]]:
    '''Фун-ия формирования строк.'''
    results = []
    for status in status_count.keys():
        row = {
            'Статус': status,
            'Количество': status_count[status]
        }
        results.append(row)
    row = {
        'Статус': 'Total',
        'Количество': total
    }
    return results