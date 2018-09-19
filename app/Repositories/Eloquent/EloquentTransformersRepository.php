<?php

namespace App\Repositories\Eloquent;

use App\Transformers;
use App\Repositories\Contracts\TransformersRepository;

use Kurt\Repoist\Repositories\Eloquent\AbstractRepository;

class EloquentTransformersRepository extends AbstractRepository implements TransformersRepository
{
    public function entity()
    {
        return Transformers::class;
    }
}
