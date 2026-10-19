def calculate_gc_content(sequence):
    """
    Вычисляет процентное содержание GC-пар в последовательности ДНК/РНК.
    """
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    if len(sequence) == 0:
        return 0.0
        
    return (g_count + c_count) / len(sequence)

def generate_kmers(sequence, k=3):
    """
    Разбивает строку ДНК на перекрывающиеся подпоследовательности длины K.
    """
    sequence = sequence.upper()
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    return kmers
