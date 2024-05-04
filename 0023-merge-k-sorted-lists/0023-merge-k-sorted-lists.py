class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Собираем все узлы в один список
        all_nodes = []
        for lst in lists:
            while lst:
                all_nodes.append(lst)
                lst = lst.next
        
        # Сортируем список узлов по значению val
        all_nodes.sort(key=lambda x: x.val)
        
        # Создаем новую голову
        dummy = ListNode()
        current = dummy
        
        # Связываем узлы в порядке возрастания значения val
        for node in all_nodes:
            current.next = node
            current = current.next
        
        return dummy.next