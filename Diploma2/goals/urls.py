from django.urls import path

from goals.views.boards import BoardCreateView, BoardListView, BoardDetailView
from goals.views.goal_category_views import CoalCategoryCreateView, GoalCategoryListView, GoalCategoryDetailView
from goals.views.goal_views import CoalCreateView, GoalListView, GoalDetailView
from goals.views.goal_comment_views import CoalCommentCreateView, GoalCommentListView, GoalCommentDetailView

urlpatterns =[
    path('board/create', BoardCreateView.as_view(), name='create-board'),
    path('board/list', BoardListView.as_view(), name='board-list'),
    path('board/<int:pk>', BoardDetailView.as_view(), name='board-details'),

    path('goal_category/create', CoalCategoryCreateView.as_view(), name='goal_category'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='list_categories'),
    path('goal_category/<int:pk>', GoalCategoryDetailView.as_view(), name='category_details'),

    path('goal/create', CoalCreateView.as_view(), name='create_goal'),
    path('goal/list', GoalListView.as_view(), name='list_goals'),
    path('goal/<int:pk>', GoalDetailView.as_view(), name='goal_details'),

    path('goal_comment/create', CoalCommentCreateView.as_view(), name='create_comment'),
    path('goal_comment/list', GoalCommentListView.as_view(), name='list_comments'),
    path('goal_comment/<int:id>', GoalCommentDetailView.as_view(), name='comment_details'),
]