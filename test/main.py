import numpy as np
import scipy.stats as stats

def simulate_data(n_control=1000, n_variant=1000, effect_size=0.05, seed=42):
    
    np.random.seed(seed)  # Устанавливаем зерно для генератора случайных чисел для повторяемости эксперимента
    base_rate = 0.1       # Базовая вероятность конверсии (например, 10%)
    # Симулируем контрольную группу с вероятностью конверсии base_rate
    control = np.random.binomial(1, base_rate, n_control)
    # Симулируем тестовую группу, в которой вероятность конверсии повышена на effect_size
    variant = np.random.binomial(1, base_rate + effect_size, n_variant)
    return control, variant

def perform_ab_test(control, variant):
    
    # Расчет средних значений конверсии для контрольной и тестовой групп
    mean_control = np.mean(control)
    mean_variant = np.mean(variant)
    print(f"Средняя конверсия (контроль): {mean_control:.3f}")
    print(f"Средняя конверсия (вариант): {mean_variant:.3f}")
    
    # Выполнение независимого t-теста.
    # Параметр equal_var=False используется, так как предполагается, что дисперсии групп могут различаться.
    t_stat, p_value = stats.ttest_ind(control, variant, equal_var=False)
    return t_stat, p_value

if __name__ == "__main__":

    # Симулируем данные для контрольной и тестовой групп
    control_group, variant_group = simulate_data()
    
    # роводим t-тест для сравнения средних значений конверсии двух групп
    t_statistic, p_value = perform_ab_test(control_group, variant_group)
    
    # Вывод результатов t-теста
    print("\nРезультаты t-теста:")
    print(f"T-статистика: {t_statistic:.3f}")
    print(f"P-value: {p_value:.3f}")
    
    # Интерпретация результатов теста
    if p_value < 0.05:
        print("Результат статистически значим (p < 0.05)")
    else:
        print("Результат не является статистически значимым (p >= 0.05)")
