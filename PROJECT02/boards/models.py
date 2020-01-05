from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=10) # length limit
    content = models.TextField() # it doesn't have length limits
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # updated_at = models.DateField()
    def __str__(self):
        return f'{self.id} - {self.title} : {self.content}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id})> -{self.content}'

# Board.objects.all()
# Board.objects.create(title='third',content='django')
# board.full_clean() method

# board.comment_set.all(); comments that the board has
