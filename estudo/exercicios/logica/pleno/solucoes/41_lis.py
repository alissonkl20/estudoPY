"""Solucao de logica/pleno/41_lis.py. Tente resolver o enunciado antes de abrir."""

def lis(nums: list[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == "__main__":
    from _rodar import rodar

    rodar(lis=lis)
